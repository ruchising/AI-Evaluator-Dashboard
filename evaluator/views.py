from django.shortcuts import render, redirect
from .models import Evaluation


def home(request):
    if request.method == "POST":
        prompt = request.POST.get('prompt')

        response1 = f"Answer explaining: {prompt}. This response focuses on clarity and correctness."
        response2 = f"Another perspective on: {prompt}. This answer is more detailed but may include extra information."

        return render(request, 'evaluate.html', {
            'prompt': prompt,
            'response1': response1,
            'response2': response2
        })

    return render(request, 'home.html')
    


def submit_evaluation(request):
    if request.method == "POST":
        Evaluation.objects.create(
            prompt=request.POST['prompt'],
            response1=request.POST['response1'],
            response2=request.POST['response2'],
            accuracy=request.POST['accuracy'],
            relevance=request.POST['relevance'],
            coherence=request.POST['coherence'],
        )
        return redirect('dashboard')



def dashboard(request):
    data = Evaluation.objects.all()

    total = len(data) if len(data) > 0 else 1

    avg_accuracy = sum([d.accuracy for d in data]) / total
    avg_relevance = sum([d.relevance for d in data]) / total
    avg_coherence = sum([d.coherence for d in data]) / total

    return render(request, 'dashboard.html', {
        'data': data,
        'avg_accuracy': avg_accuracy,
        'avg_relevance': avg_relevance,
        'avg_coherence': avg_coherence
    })