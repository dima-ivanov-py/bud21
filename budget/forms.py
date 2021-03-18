from django import forms

from .models import Balance, Profit, Expense


class BalanceEditForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    total = forms.DecimalField(
        label='Total',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-lg',
                'min':'-1000000',
                'max':'1000000',
                'step':'.01'
            }
        )
    )
    class Meta:
        model = Balance
        fields = ('title', 'total')


class ProfitEditForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Profit
        fields = ('title', 'description')


class ExpenseEditForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    description = forms.CharField(
        label='Description',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    class Meta:
        model = Expense
        fields = ('title', 'description')
