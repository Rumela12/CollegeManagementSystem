
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views, HOD_views, professor_views, student_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),
    path('',views.HOME,name='home' ),

    #login path
    path('Login', views.LOGIN, name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    #profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE, name='profile_update'),

    #this is hod panel
    path('HOD/home', HOD_views.HOME,name='hod_home'),
    path('HOD/Student/Add',HOD_views.ADD_STUDENTS,name='add_student'),
    path('HOD/Student/View',HOD_views.VIEW_STUDENT,name='view_student'),
    path('HOD/Student/Edit/<str:id>',HOD_views.EDIT_STUDENT,name= 'edit_student'),
    path('HOD/Student/Update',HOD_views.UPDATE_STUDENT, name='update_student'),
    path('HOD/Student/Delete/<str:admin>',HOD_views.DELETE_STUDENT, name='delete_student'),

    path('HOD/Professor/Add',HOD_views.ADD_STAFF,name="add_staff"),
    path('HOD/Professor/View', HOD_views.VIEW_STAFF, name='view_staff'),
    path('HOD/Professor/Edit/<str:id>', HOD_views.EDIT_STAFF, name='edit_staff'),
    path('HOD/Professor/Update', HOD_views.UPDATE_STAFF, name='update_staff'),
    path('HOD/Professor/Delete/<str:admin>', HOD_views.DELETE_STAFF, name='delete_staff'),

    path('HOD/Course/Add',HOD_views.ADD_COURSE,name='add_course'),
    path('HOD/Course/View', HOD_views.VIEW_COURSE, name='view_course'),
    path('HOD/Course/Edit/<str:id>', HOD_views.EDIT_COURSE, name='edit_course'),
    path('HOD/Course/Update', HOD_views.UPDATE_COURSE, name='update_course'),
    path('HOD/Course/Delete/<str:id>', HOD_views.DELETE_COURSE, name='delete_course'),

    path('HOD/Subject/Add', HOD_views.ADD_SUBJECT, name='add_subject'),
    path('HOD/Subject/View', HOD_views.VIEW_SUBJECT, name='view_subject'),
    path('HOD/Subject/Edit/<str:id>', HOD_views.EDIT_SUBJECT, name='edit_subject'),
    path('HOD/Subject/Update', HOD_views.UPDATE_SUBJECT, name='update_subject'),
    path('HOD/Subject/Delete/<str:id>', HOD_views.DELETE_SUBJECT, name='delete_subject'),

    path('HOD/Session/Add', HOD_views.ADD_SESSION, name='add_session'),
    path('HOD/Session/View', HOD_views.VIEW_SESSION, name='view_session'),
    path('HOD/Session/Edit/<str:id>', HOD_views.EDIT_SESSION, name='edit_session'),
    path('HOD/Session/Update', HOD_views.UPDATE_SESSION, name='update_session'),
    path('HOD/Session/Delete/<str:id>', HOD_views.DELETE_SESSION, name='delete_session'),

    path('HOD/Professor/Send_Notification',HOD_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('HOD/Professor/Save_Notification', HOD_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('HOD/Student/Send_Notification', HOD_views.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
    path('HOD/Student/Save_Notification', HOD_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),

    path('HOD/Professor/Leave_view',HOD_views.Staff_Leave_view, name='staff_leave_view'),
    path('HOD/Professor/approve_leave/<str:id>', HOD_views.STAFF_APPROVE_LEAVE, name='staff_approve_leave'),
    path('HOD/Professor/reject_leave/<str:id>', HOD_views.STAFF_DISAPPROVE_LEAVE, name='staff_disapprove_leave'),

    path('HOD/Student/Leave_view',HOD_views.STUDENT_LEAVE_VIEW, name='student_leave_view'),
    path('HOD/Student/approve_leave/<str:id>', HOD_views.STUDENT_APPROVE_LEAVE, name='student_approve_leave'),
    path('HOD/Student/reject_leave/<str:id>', HOD_views.STUDENT_DISAPPROVE_LEAVE, name='student_disapprove_leave'),

    path('HOD/Professor/Feedback', HOD_views.STAFF_FEEDBACK, name='staff_feedback_reply'),
    path('HOD/Professor/Feedback/save', HOD_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_reply_save'),

    path('HOD/Student/Feedback', HOD_views.STUDENT_FEEDBACK, name='student_feedback_reply'),
    path('HOD/Student/Feedback/save', HOD_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_reply_save'),

    path('HOD/View/Attendance', HOD_views.VIEW_ATTENDANCE,name='view_attendance'),

   #this is professor panel
    path('Professor/Home',professor_views.HOME,name='staff_home'),

    path('Professor/Notifications',professor_views.NOTIFICATIONS,name='notifications'),
    path('Professor/mark_as_done/<str:status>',professor_views.STAFF_NOTIFICATION_MARK_AS_DONE,name='staff_notification_mark_as_done'),

    path('Professor/Apply_leave',professor_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Professor/Apply_leave_save', professor_views.STAFF_APPLY_LEAVE_SAVE, name='staff_apply_leave_save'),

    path('Professor/Feedback', professor_views.STAFF_FEEDBACK,name='staff_feedback'),
    path('Professor/Feedback/Save', professor_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

    path('Professor/Take_Attendance', professor_views.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('Professor/Save_Attendance', professor_views.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('Professor/View_Attendance', professor_views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),

    path('Professor/Add_Result', professor_views.STAFF_ADD_RESULT,name='staff_add_result'),
    path('Professor/Save/Result', professor_views.STAFF_SAVE_RESULT, name='staff_save_result'),

                  #this is student panel

    path('Student/Home', student_views.HOME, name='student_home'),
    path('Student/Notifications', student_views.STUDENT_NOTIFICATION, name='student_notification'),
    path('Student/mark_as_done/<str:status>', student_views.STUDENT_NOTIFICATION_MARK_AS_DONE,name='student_notification_mark_as_done'),


    path('Student/Feedback', student_views.STUDENT_FEEDBACK,name='student_feedback'),
    path('Student/Feedback/Save', student_views.STUDENT_FEEDBACK_SAVE, name='student_feedback_save'),

    path('Student/Apply_leave',student_views.STUDENT_LEAVE,name='student_leave'),
    path('Student/Apply_leave_save', student_views.STUDENT_LEAVE_SAVE, name='student_leave_save'),

    path('Student/View_Attendance', student_views.STUDENT_VIEW_ATTENDACE, name='student_view_attendance'),
    path('Student/View_Result', student_views.VIEW_RESULT, name='view_result'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
