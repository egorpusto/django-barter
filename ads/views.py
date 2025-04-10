from django.shortcuts import render, get_object_or_404, redirect
from .models import Ad, ExchangeProposal
from .forms import AdForm, ExchangeProposalForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Показать все объявления
def ad_list(request):
    ads = Ad.objects.all().order_by('-created_at')

    query = request.GET.get('q')
    category = request.GET.get('category')
    condition = request.GET.get('condition')

    if query:
        ads = ads.filter(title__icontains=query) | ads.filter(
            description__icontains=query)

    if category:
        ads = ads.filter(category__icontains=category)

    if condition:
        ads = ads.filter(condition=condition)

    return render(request, 'ads/ad_list.html', {
        'ads': ads,
        'query': query,
        'category': category,
        'condition': condition,
    })


# Создать новое объявление
@login_required
def ad_create(request):
    if request.method == 'POST':
        form = AdForm(request.POST)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.user = request.user  # автор объявления
            ad.save()
            return redirect('ad_list')
    else:
        form = AdForm()
    return render(request, 'ads/ad_form.html', {'form': form})


# Редактировать своё объявление
@login_required
def ad_edit(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if ad.user != request.user:
        return HttpResponseForbidden("Вы не можете редактировать это объявление.")

    if request.method == 'POST':
        form = AdForm(request.POST, instance=ad)
        if form.is_valid():
            form.save()
            return redirect('ad_list')
    else:
        form = AdForm(instance=ad)
    return render(request, 'ads/ad_form.html', {'form': form})


# Удалить своё объявление
@login_required
def ad_delete(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    if ad.user != request.user:
        return HttpResponseForbidden("Вы не можете удалить это объявление.")

    if request.method == 'POST':
        ad.delete()
        return redirect('ad_list')

    return render(request, 'ads/ad_confirm_delete.html', {'ad': ad})


# Для создания предложения
@login_required
def create_proposal(request):
    if request.method == 'POST':
        form = ExchangeProposalForm(request.POST)
        if form.is_valid():
            proposal = form.save(commit=False)
            proposal.status = 'pending'  # устанавливаем статус по умолчанию
            proposal.save()
            return redirect('proposal_list')
    else:
        form = ExchangeProposalForm()
    return render(request, 'ads/proposal_form.html', {'form': form})


# Для списка предложений
@login_required
def proposal_list(request):
    proposals = ExchangeProposal.objects.filter(
        ad_receiver__user=request.user
    ).order_by('-created_at')
    return render(request, 'ads/proposal_list.html', {'proposals': proposals})


# Для обновления статуса предложения
@login_required
def update_proposal_status(request, pk, status):
    proposal = get_object_or_404(ExchangeProposal, pk=pk)
    if proposal.ad_receiver.user != request.user:
        return HttpResponseForbidden("Вы не можете менять это предложение.")

    if status in ['accepted', 'declined']:
        proposal.status = status
        proposal.save()

    return redirect('proposal_list')
