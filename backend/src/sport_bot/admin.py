from django.contrib import admin
from . import models


# Register your models here.

class SportBotAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'username', 'gender', 'phone_number']
    list_editable = ['first_name', 'username', 'gender', 'phone_number']


class StandardsAdmin(admin.ModelAdmin):
    list_display = ['id', 'thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell', 'bench_press', 'axel_jerk',
                    'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk', 'taking_on_the_chest',
                    'axel_deadlift',
                    'classic_squat', 'front_squat', 'squat_over_the_head', 'skipping_rope', 'push_ups',
                    'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump', 'holding_the_axel',
                    'handstand']
    list_editable = ['thunder', 'turkish_ascent_axel', 'turkish_ascent_kettlebell', 'bench_press', 'axel_jerk',
                     'taking_on_axel_chest', 'gluteal_bridge', 'deadlift', 'jerk', 'taking_on_the_chest',
                     'axel_deadlift',
                     'classic_squat', 'front_squat', 'squat_over_the_head', 'skipping_rope', 'push_ups',
                     'shuttle_running', 'farmer_walk', 'pull_ups', 'high_jump', 'long_jump', 'holding_the_axel',
                     'handstand']


class ProfileUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'training_history', 'number_of_referral_points', 'info_subscription', 'current_standard']
    list_editable = ['training_history', 'number_of_referral_points', 'info_subscription', 'current_standard']


admin.site.register(models.User, SportBotAdmin)
admin.site.register(models.Standards, StandardsAdmin)
admin.site.register(models.Profile, ProfileUserAdmin)
