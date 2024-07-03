from .models import Standards, Statistics, StatisticsGet
from django.forms import ModelForm
from django import forms


class StandardsForm(ModelForm):
    class Meta:
        model = Standards
        fields = ['telegram_id', 'first_name', 'thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell', 'bench_press',
                  'axel_jerk', 'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk', 'taking_on_the_chest',
                  'axel_deadlift', 'classic_squat', 'front_squat', 'squat_over_the_head', 'skipping_rope',
                  'push_ups', 'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump',
                  'holding_the_axel',
                  'handstand']

        widgets = {
            'telegram_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID из telegram',
                'label': 'Имя пользователя',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя из CRM',
            }),
            'thunder': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'turkish_ascent_axel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'turkish_ascent_kettlebell': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'bench_press': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'axel_jerk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'taking_on_axel_chest': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'gluteal_bridge': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'deadlift': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'jerk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'taking_on_the_chest': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'axel_deadlift': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'classic_squat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'front_squat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'squat_over_the_head': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'skipping_rope': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'push_ups': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'shuttle_running': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'farmer_walk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'pull_ups': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'high_jump': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'long_jump': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'holding_the_axel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'handstand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
        }


class StatisticsForm(ModelForm):
    class Meta:
        model = Statistics
        fields = ['user_id', 'user_name', 'thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell',
                  'bench_press',
                  'axel_jerk', 'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk', 'taking_on_the_chest',
                  'axel_deadlift', 'classic_squat', 'front_squat', 'squat_over_the_head', 'skipping_rope',
                  'push_ups', 'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump',
                  'holding_the_axel',
                  'handstand', 'month', 'year']

        widgets = {
            'user_id': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ID из телеграмм',
            }),
            'user_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя из CRM',
            }),
            'thunder': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'turkish_ascent_axel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'turkish_ascent_kettlebell': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'bench_press': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'axel_jerk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'taking_on_axel_chest': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'gluteal_bridge': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'deadlift': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'jerk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'taking_on_the_chest': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'axel_deadlift': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'classic_squat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'front_squat': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'squat_over_the_head': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'skipping_rope': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'push_ups': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'shuttle_running': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'farmer_walk': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'pull_ups': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'high_jump': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'long_jump': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'holding_the_axel': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'handstand': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Значение норматива'
            }),
            'month': forms.Select(attrs={
                'class': 'form-select'
            }),
            'year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год'
            }),
        }


class StatisticsFormGet(ModelForm):
    class Meta:
        model = StatisticsGet
        fields = ['standard', 'year']

        widgets = {
            'standard': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'example: Гром',
            }),
            'year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Год',
            }),
        }
