# poll/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Poll, Vote, Choice, Question
from django.utils import timezone
from django.db.models import Count, Q
import csv
from django.http import HttpResponse
from django.views.decorators.http import require_POST

def index_view(request):
    """
    This view will render our new public homepage.
    """
    return render(request, 'poll/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('poll_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('poll_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@require_POST
def logout_view(request):
    """
    Logs the user out and redirects to the homepage.
    The @require_POST decorator ensures this can only be called via a POST request,
    which prevents accidental logouts and helps with CSRF.
    """
    logout(request)
    return redirect('index')

@login_required
def poll_list(request):
    polls = Poll.objects.filter(start_date__lte=timezone.now()).filter(
        Q(end_date__gte=timezone.now()) | Q(end_date__isnull=True)
    )
    return render(request, 'poll/poll_list.html', {'polls': polls})

@login_required
def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    user_has_voted = Vote.objects.filter(user=request.user, poll=poll).exists()
    return render(request, 'poll/poll_detail.html', {'poll': poll, 'user_has_voted': user_has_voted})

@login_required
def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if not poll.is_active() or Vote.objects.filter(user=request.user, poll=poll).exists():
        return redirect('poll_detail', poll_id=poll.id)

    if request.method == 'POST':
        for question in poll.questions.all():
            choice_id = request.POST.get(f'question_{question.id}')
            if choice_id:
                choice = get_object_or_404(Choice, pk=choice_id)
                Vote.objects.create(user=request.user, poll=poll, question=question, choice=choice)
        return redirect('poll_results', poll_id=poll.id)
    return render(request, 'poll/vote.html', {'poll': poll})

@login_required
def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    results = {}

    for question in poll.questions.all():
        # Get choices and their vote counts
        choices_with_votes = question.choices.annotate(vote_count=Count('vote'))
        
        # Calculate the total votes for this specific question
        total_votes = sum(c.vote_count for c in choices_with_votes)

        # *** THIS IS THE NEW LOGIC ***
        # Loop through the choices again to calculate and attach the percentage
        for choice in choices_with_votes:
            if total_votes > 0:
                choice.percentage = (choice.vote_count / total_votes) * 100
            else:
                choice.percentage = 0  # Avoid division by zero

        # Pass the enhanced data to the results dictionary
        results[question] = {
            'choices': choices_with_votes, 
            'total_votes': total_votes
        }

    return render(request, 'poll/poll_results.html', {'poll': poll, 'results': results})

@login_required
def my_votes(request):
    votes = Vote.objects.filter(user=request.user).select_related('poll', 'question', 'choice')
    return render(request, 'poll/my_votes.html', {'votes': votes})

@login_required
def export_results_csv(request, poll_id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="poll_{poll_id}_results.csv"'

    writer = csv.writer(response)
    poll = get_object_or_404(Poll, pk=poll_id)
    writer.writerow(['Question', 'Choice', 'Number of Votes'])

    for question in poll.questions.all():
        for choice in question.choices.annotate(vote_count=Count('vote')):
            writer.writerow([question.question_text, choice.choice_text, choice.vote_count])
    return response