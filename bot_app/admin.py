from django.contrib import admin
from bot_app.models import Standards, Profile, Statistics

# Register your models here.


class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'first_name', 'username', 'gender', 'phone_number',
                    'training_history', 'number_of_referral_points', 'info_subscription', 'current_standard']

    list_editable = ['username', 'gender', 'phone_number', 'training_history',
                     'number_of_referral_points', 'info_subscription', 'current_standard']

    list_filter = ['gender']

    search_fields = ['first_name', 'phone_number']


class StandardsAdmin(admin.ModelAdmin):
    list_display = ['telegram_id', 'first_name', 'thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell',
                    'bench_press', 'axel_jerk', 'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk',
                    'taking_on_the_chest', 'axel_deadlift', 'classic_squat', 'front_squat', 'squat_over_the_head',
                    'skipping_rope', 'push_ups', 'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump',
                    'holding_the_axel', 'handstand']

    list_editable = ['thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell', 'bench_press',
                     'axel_jerk', 'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk', 'taking_on_the_chest',
                     'axel_deadlift', 'classic_squat', 'front_squat', 'squat_over_the_head', 'skipping_rope',
                     'push_ups',
                     'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump', 'holding_the_axel',
                     'handstand']

    list_filter = ['first_name']


class StatisticsAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'user_name', 'thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell',
                    'bench_press', 'axel_jerk', 'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk',
                    'taking_on_the_chest', 'axel_deadlift', 'classic_squat', 'front_squat', 'squat_over_the_head',
                    'skipping_rope', 'push_ups', 'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump',
                    'holding_the_axel', 'handstand', 'month', 'year']

    list_editable = ['thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell',
                     'bench_press', 'axel_jerk', 'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk',
                     'taking_on_the_chest', 'axel_deadlift', 'classic_squat', 'front_squat', 'squat_over_the_head',
                     'skipping_rope', 'push_ups', 'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump',
                     'holding_the_axel', 'handstand', 'month', 'year']

    list_filter = ['month', 'year']

    search_fields = ['user_id', 'user_name']


admin.site.register(Standards, StandardsAdmin)
admin.site.register(Profile, ProfileUserAdmin)
admin.site.register(Statistics, StatisticsAdmin)
