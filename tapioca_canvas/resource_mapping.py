# coding: utf-8

RESOURCE_MAPPING = {
    "account_domain_lookups_search": {
        "resource": "/api/v1/accounts/search",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_domain_lookups.search"
    },
    "account_notifications_user_index": {
        "resource": "/api/v1/accounts/{account_id}/users/{user_id}/account_notifications",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_notifications.user_index"
    },
    "account_notifications_show": {
        "resource": "/api/v1/accounts/{account_id}/users/{user_id}/account_notifications/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_notifications.show"
    },
    "account_notifications_user_close_notification": {
        "resource": "/api/v1/accounts/{account_id}/users/{user_id}/account_notifications/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_notifications.user_close_notification"
    },
    "account_notifications_create": {
        "resource": "/api/v1/accounts/{account_id}/account_notifications",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_notifications.create"
    },
    "account_notifications_update": {
        "resource": "/api/v1/accounts/{account_id}/account_notifications/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_notifications.update"
    },
    "account_reports_available_reports": {
        "resource": "/api/v1/accounts/{account_id}/reports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_reports.available_reports"
    },
    "account_reports_create": {
        "resource": "/api/v1/accounts/{account_id}/reports/{report}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_reports.create"
    },
    "account_reports_index": {
        "resource": "/api/v1/accounts/{account_id}/reports/{report}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_reports.index"
    },
    "account_reports_show": {
        "resource": "/api/v1/accounts/{account_id}/reports/{report}/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_reports.show"
    },
    "account_reports_destroy": {
        "resource": "/api/v1/accounts/{account_id}/reports/{report}/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_reports.destroy"
    },
    "accounts_index": {
        "resource": "/api/v1/accounts",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.index"
    },
    "accounts_course_accounts": {
        "resource": "/api/v1/course_accounts",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.course_accounts"
    },
    "accounts_show": {
        "resource": "/api/v1/accounts/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.show"
    },
    "accounts_sub_accounts": {
        "resource": "/api/v1/accounts/{account_id}/sub_accounts",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.sub_accounts"
    },
    "accounts_terms_of_service": {
        "resource": "/api/v1/accounts/{account_id}/terms_of_service",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.terms_of_service"
    },
    "accounts_courses_api": {
        "resource": "/api/v1/accounts/{account_id}/courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.courses_api"
    },
    "accounts_update": {
        "resource": "/api/v1/accounts/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.update"
    },
    "accounts_remove_user": {
        "resource": "/api/v1/accounts/{account_id}/users/{user_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.accounts.remove_user"
    },
    "sub_accounts_create": {
        "resource": "/api/v1/accounts/{account_id}/sub_accounts",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sub_accounts.create"
    },
    "sub_accounts_destroy": {
        "resource": "/api/v1/accounts/{account_id}/sub_accounts/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sub_accounts.destroy"
    },
    "admins_create": {
        "resource": "/api/v1/accounts/{account_id}/admins",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.admins.create"
    },
    "admins_destroy": {
        "resource": "/api/v1/accounts/{account_id}/admins/{user_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.admins.destroy"
    },
    "admins_index": {
        "resource": "/api/v1/accounts/{account_id}/admins",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.admins.index"
    },
    "analytics_api_department_participation": {
        "resource": "/api/v1/accounts/{account_id}/analytics/terms/{term_id}/activity",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.department_participation"
    },
    "analytics_api_department_grades": {
        "resource": "/api/v1/accounts/{account_id}/analytics/terms/{term_id}/grades",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.department_grades"
    },
    "analytics_api_department_statistics": {
        "resource": "/api/v1/accounts/{account_id}/analytics/terms/{term_id}/statistics",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.department_statistics"
    },
    "analytics_api_course_participation": {
        "resource": "/api/v1/courses/{course_id}/analytics/activity",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.course_participation"
    },
    "analytics_api_course_assignments": {
        "resource": "/api/v1/courses/{course_id}/analytics/assignments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.course_assignments"
    },
    "analytics_api_course_student_summaries": {
        "resource": "/api/v1/courses/{course_id}/analytics/student_summaries",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.course_student_summaries"
    },
    "analytics_api_student_in_course_participation": {
        "resource": "/api/v1/courses/{course_id}/analytics/users/{student_id}/activity",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.student_in_course_participation"
    },
    "analytics_api_student_in_course_assignments": {
        "resource": "/api/v1/courses/{course_id}/analytics/users/{student_id}/assignments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.student_in_course_assignments"
    },
    "analytics_api_student_in_course_messaging": {
        "resource": "/api/v1/courses/{course_id}/analytics/users/{student_id}/communication",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.analytics_api.student_in_course_messaging"
    },
    "external_feeds_index": {
        "resource": "/api/v1/courses/{course_id}/external_feeds",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_feeds.index"
    },
    "external_feeds_create": {
        "resource": "/api/v1/courses/{course_id}/external_feeds",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_feeds.create"
    },
    "external_feeds_destroy": {
        "resource": "/api/v1/courses/{course_id}/external_feeds/{external_feed_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_feeds.destroy"
    },
    "announcements_api_index": {
        "resource": "/api/v1/announcements",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.announcements_api.index"
    },
    "appointment_groups_index": {
        "resource": "/api/v1/appointment_groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.index"
    },
    "appointment_groups_create": {
        "resource": "/api/v1/appointment_groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.create"
    },
    "appointment_groups_show": {
        "resource": "/api/v1/appointment_groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.show"
    },
    "appointment_groups_update": {
        "resource": "/api/v1/appointment_groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.update"
    },
    "appointment_groups_destroy": {
        "resource": "/api/v1/appointment_groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.destroy"
    },
    "appointment_groups_users": {
        "resource": "/api/v1/appointment_groups/{id}/users",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.users"
    },
    "appointment_groups_groups": {
        "resource": "/api/v1/appointment_groups/{id}/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.groups"
    },
    "appointment_groups_next_appointment": {
        "resource": "/api/v1/appointment_groups/next_appointment",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.appointment_groups.next_appointment"
    },
    "assignment_groups_index": {
        "resource": "/api/v1/courses/{course_id}/assignment_groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_groups.index"
    },
    "assignment_groups_api_show": {
        "resource": "/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_groups_api.show"
    },
    "assignment_groups_api_create": {
        "resource": "/api/v1/courses/{course_id}/assignment_groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_groups_api.create"
    },
    "assignment_groups_api_update": {
        "resource": "/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_groups_api.update"
    },
    "assignment_groups_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_groups_api.destroy"
    },
    "assignments_destroy": {
        "resource": "/api/v1/courses/{course_id}/assignments/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignments.destroy"
    },
    "assignments_api_index": {
        "resource": "/api/v1/courses/{course_id}/assignments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignments_api.index"
    },
    "assignments_api_user_index": {
        "resource": "/api/v1/users/{user_id}/courses/{course_id}/assignments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignments_api.user_index"
    },
    "assignments_api_show": {
        "resource": "/api/v1/courses/{course_id}/assignments/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignments_api.show"
    },
    "assignments_api_create": {
        "resource": "/api/v1/courses/{course_id}/assignments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignments_api.create"
    },
    "assignments_api_update": {
        "resource": "/api/v1/courses/{course_id}/assignments/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignments_api.update"
    },
    "assignment_overrides_index": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.index"
    },
    "assignment_overrides_show": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.show"
    },
    "assignment_overrides_group_alias": {
        "resource": "/api/v1/groups/{group_id}/assignments/{assignment_id}/override",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.group_alias"
    },
    "assignment_overrides_section_alias": {
        "resource": "/api/v1/sections/{course_section_id}/assignments/{assignment_id}/override",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.section_alias"
    },
    "assignment_overrides_create": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.create"
    },
    "assignment_overrides_update": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.update"
    },
    "assignment_overrides_destroy": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.destroy"
    },
    "assignment_overrides_batch_retrieve": {
        "resource": "/api/v1/courses/{course_id}/assignments/overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.batch_retrieve"
    },
    "assignment_overrides_batch_create": {
        "resource": "/api/v1/courses/{course_id}/assignments/overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.batch_create"
    },
    "assignment_overrides_batch_update": {
        "resource": "/api/v1/courses/{course_id}/assignments/overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.assignment_overrides.batch_update"
    },
    "account_authorization_configs_index": {
        "resource": "/api/v1/accounts/{account_id}/authentication_providers",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_authorization_configs.index"
    },
    "account_authorization_configs_create": {
        "resource": "/api/v1/accounts/{account_id}/authentication_providers",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_authorization_configs.create"
    },
    "account_authorization_configs_update": {
        "resource": "/api/v1/accounts/{account_id}/authentication_providers/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_authorization_configs.update"
    },
    "account_authorization_configs_show": {
        "resource": "/api/v1/accounts/{account_id}/authentication_providers/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_authorization_configs.show"
    },
    "account_authorization_configs_destroy": {
        "resource": "/api/v1/accounts/{account_id}/authentication_providers/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_authorization_configs.destroy"
    },
    "account_authorization_configs_show_sso_settings": {
        "resource": "/api/v1/accounts/{account_id}/sso_settings",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_authorization_configs.show_sso_settings"
    },
    "account_authorization_configs_update_sso_settings": {
        "resource": "/api/v1/accounts/{account_id}/sso_settings",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.account_authorization_configs.update_sso_settings"
    },
    "authentication_audit_api_for_login": {
        "resource": "/api/v1/audit/authentication/logins/{login_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.authentication_audit_api.for_login"
    },
    "authentication_audit_api_for_account": {
        "resource": "/api/v1/audit/authentication/accounts/{account_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.authentication_audit_api.for_account"
    },
    "authentication_audit_api_for_user": {
        "resource": "/api/v1/audit/authentication/users/{user_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.authentication_audit_api.for_user"
    },
    "master_courses/master_templates_show": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.show"
    },
    "master_courses/master_templates_associated_courses": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/associated_courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.associated_courses"
    },
    "master_courses/master_templates_update_associations": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.update_associations"
    },
    "master_courses/master_templates_queue_migration": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.queue_migration"
    },
    "master_courses/master_templates_restrict_item": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/restrict_item",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.restrict_item"
    },
    "master_courses/master_templates_unsynced_changes": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/unsynced_changes",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.unsynced_changes"
    },
    "master_courses/master_templates_migrations_index": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.migrations_index"
    },
    "master_courses/master_templates_migrations_show": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.migrations_show"
    },
    "master_courses/master_templates_migration_details": {
        "resource": "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}/details",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.migration_details"
    },
    "master_courses/master_templates_imports_index": {
        "resource": "/api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.imports_index"
    },
    "master_courses/master_templates_imports_show": {
        "resource": "/api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.imports_show"
    },
    "master_courses/master_templates_import_details": {
        "resource": "/api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}/details",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.master_courses/master_templates.import_details"
    },
    "bookmarks/bookmarks_index": {
        "resource": "/api/v1/users/self/bookmarks",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.bookmarks/bookmarks.index"
    },
    "bookmarks/bookmarks_create": {
        "resource": "/api/v1/users/self/bookmarks",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.bookmarks/bookmarks.create"
    },
    "bookmarks/bookmarks_show": {
        "resource": "/api/v1/users/self/bookmarks/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.bookmarks/bookmarks.show"
    },
    "bookmarks/bookmarks_update": {
        "resource": "/api/v1/users/self/bookmarks/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.bookmarks/bookmarks.update"
    },
    "bookmarks/bookmarks_destroy": {
        "resource": "/api/v1/users/self/bookmarks/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.bookmarks/bookmarks.destroy"
    },
    "brand_configs_api_show": {
        "resource": "/api/v1/brand_variables",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.brand_configs_api.show"
    },
    "calendar_events_api_index": {
        "resource": "/api/v1/calendar_events",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.index"
    },
    "calendar_events_api_user_index": {
        "resource": "/api/v1/users/{user_id}/calendar_events",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.user_index"
    },
    "calendar_events_api_create": {
        "resource": "/api/v1/calendar_events",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.create"
    },
    "calendar_events_api_show": {
        "resource": "/api/v1/calendar_events/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.show"
    },
    "calendar_events_api_reserve": {
        "resource": "/api/v1/calendar_events/{id}/reservations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.reserve"
    },
    "calendar_events_api_update": {
        "resource": "/api/v1/calendar_events/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.update"
    },
    "calendar_events_api_destroy": {
        "resource": "/api/v1/calendar_events/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.destroy"
    },
    "calendar_events_api_set_course_timetable": {
        "resource": "/api/v1/courses/{course_id}/calendar_events/timetable",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.set_course_timetable"
    },
    "calendar_events_api_get_course_timetable": {
        "resource": "/api/v1/courses/{course_id}/calendar_events/timetable",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.get_course_timetable"
    },
    "calendar_events_api_set_course_timetable_events": {
        "resource": "/api/v1/courses/{course_id}/calendar_events/timetable_events",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.calendar_events_api.set_course_timetable_events"
    },
    "collaborations_api_index": {
        "resource": "/api/v1/courses/{course_id}/collaborations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.collaborations.api_index"
    },
    "collaborations_members": {
        "resource": "/api/v1/collaborations/{id}/members",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.collaborations.members"
    },
    "collaborations_potential_collaborators": {
        "resource": "/api/v1/courses/{course_id}/potential_collaborators",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.collaborations.potential_collaborators"
    },
    "comm_messages_api_index": {
        "resource": "/api/v1/comm_messages",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.comm_messages_api.index"
    },
    "communication_channels_index": {
        "resource": "/api/v1/users/{user_id}/communication_channels",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.communication_channels.index"
    },
    "communication_channels_create": {
        "resource": "/api/v1/users/{user_id}/communication_channels",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.communication_channels.create"
    },
    "communication_channels_destroy": {
        "resource": "/api/v1/users/{user_id}/communication_channels/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.communication_channels.destroy"
    },
    "conferences_index": {
        "resource": "/api/v1/courses/{course_id}/conferences",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conferences.index"
    },
    "content_exports_api_index": {
        "resource": "/api/v1/courses/{course_id}/content_exports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_exports_api.index"
    },
    "content_exports_api_show": {
        "resource": "/api/v1/courses/{course_id}/content_exports/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_exports_api.show"
    },
    "content_exports_api_create": {
        "resource": "/api/v1/courses/{course_id}/content_exports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_exports_api.create"
    },
    "migration_issues_index": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.migration_issues.index"
    },
    "migration_issues_show": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.migration_issues.show"
    },
    "migration_issues_update": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.migration_issues.update"
    },
    "content_migrations_index": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_migrations.index"
    },
    "content_migrations_show": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_migrations.show"
    },
    "content_migrations_create": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_migrations.create"
    },
    "content_migrations_update": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_migrations.update"
    },
    "content_migrations_available_migrators": {
        "resource": "/api/v1/accounts/{account_id}/content_migrations/migrators",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_migrations.available_migrators"
    },
    "conversations_index": {
        "resource": "/api/v1/conversations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.index"
    },
    "conversations_create": {
        "resource": "/api/v1/conversations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.create"
    },
    "conversations_batches": {
        "resource": "/api/v1/conversations/batches",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.batches"
    },
    "conversations_show": {
        "resource": "/api/v1/conversations/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.show"
    },
    "conversations_update": {
        "resource": "/api/v1/conversations/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.update"
    },
    "conversations_mark_all_as_read": {
        "resource": "/api/v1/conversations/mark_all_as_read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.mark_all_as_read"
    },
    "conversations_destroy": {
        "resource": "/api/v1/conversations/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.destroy"
    },
    "conversations_add_recipients": {
        "resource": "/api/v1/conversations/{id}/add_recipients",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.add_recipients"
    },
    "conversations_add_message": {
        "resource": "/api/v1/conversations/{id}/add_message",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.add_message"
    },
    "conversations_remove_messages": {
        "resource": "/api/v1/conversations/{id}/remove_messages",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.remove_messages"
    },
    "conversations_batch_update": {
        "resource": "/api/v1/conversations",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.batch_update"
    },
    "conversations_find_recipients": {
        "resource": "/api/v1/conversations/find_recipients",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.find_recipients"
    },
    "conversations_unread_count": {
        "resource": "/api/v1/conversations/unread_count",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.conversations.unread_count"
    },
    "course_audit_api_for_course": {
        "resource": "/api/v1/audit/course/courses/{course_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.course_audit_api.for_course"
    },
    "quizzes/course_quiz_extensions_create": {
        "resource": "/api/v1/courses/{course_id}/quiz_extensions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/course_quiz_extensions.create"
    },
    "courses_index": {
        "resource": "/api/v1/courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.index"
    },
    "courses_user_index": {
        "resource": "/api/v1/users/{user_id}/courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.user_index"
    },
    "courses_create": {
        "resource": "/api/v1/accounts/{account_id}/courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.create"
    },
    "courses_create_file": {
        "resource": "/api/v1/courses/{course_id}/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.create_file"
    },
    "courses_students": {
        "resource": "/api/v1/courses/{course_id}/students",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.students"
    },
    "courses_users": {
        "resource": "/api/v1/courses/{course_id}/users",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.users"
    },
    "courses_recent_students": {
        "resource": "/api/v1/courses/{course_id}/recent_students",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.recent_students"
    },
    "courses_user": {
        "resource": "/api/v1/courses/{course_id}/users/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.user"
    },
    "courses_preview_html": {
        "resource": "/api/v1/courses/{course_id}/preview_html",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.preview_html"
    },
    "courses_activity_stream": {
        "resource": "/api/v1/courses/{course_id}/activity_stream",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.activity_stream"
    },
    "courses_activity_stream_summary": {
        "resource": "/api/v1/courses/{course_id}/activity_stream/summary",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.activity_stream_summary"
    },
    "courses_todo_items": {
        "resource": "/api/v1/courses/{course_id}/todo",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.todo_items"
    },
    "courses_destroy": {
        "resource": "/api/v1/courses/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.destroy"
    },
    "courses_settings": {
        "resource": "/api/v1/courses/{course_id}/settings",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.settings"
    },
    "courses_update_settings": {
        "resource": "/api/v1/courses/{course_id}/settings",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.update_settings"
    },
    "courses_show": {
        "resource": "/api/v1/courses/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.show"
    },
    "courses_update": {
        "resource": "/api/v1/courses/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.update"
    },
    "courses_batch_update": {
        "resource": "/api/v1/accounts/{account_id}/courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.batch_update"
    },
    "courses_reset_content": {
        "resource": "/api/v1/courses/{course_id}/reset_content",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.reset_content"
    },
    "courses_effective_due_dates": {
        "resource": "/api/v1/courses/{course_id}/effective_due_dates",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.effective_due_dates"
    },
    "courses_permissions": {
        "resource": "/api/v1/courses/{course_id}/permissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.courses.permissions"
    },
    "content_imports_copy_course_status": {
        "resource": "/api/v1/courses/{course_id}/course_copy/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_imports.copy_course_status"
    },
    "content_imports_copy_course_content": {
        "resource": "/api/v1/courses/{course_id}/course_copy",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.content_imports.copy_course_content"
    },
    "custom_gradebook_columns_api_index": {
        "resource": "/api/v1/courses/{course_id}/custom_gradebook_columns",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_gradebook_columns_api.index"
    },
    "custom_gradebook_columns_api_create": {
        "resource": "/api/v1/courses/{course_id}/custom_gradebook_columns",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_gradebook_columns_api.create"
    },
    "custom_gradebook_columns_api_update": {
        "resource": "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_gradebook_columns_api.update"
    },
    "custom_gradebook_columns_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_gradebook_columns_api.destroy"
    },
    "custom_gradebook_columns_api_reorder": {
        "resource": "/api/v1/courses/{course_id}/custom_gradebook_columns/reorder",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_gradebook_columns_api.reorder"
    },
    "custom_gradebook_column_data_api_index": {
        "resource": "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_gradebook_column_data_api.index"
    },
    "custom_gradebook_column_data_api_update": {
        "resource": "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data/{user_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_gradebook_column_data_api.update"
    },
    "discussion_topics_index": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics.index"
    },
    "discussion_topics_create": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics.create"
    },
    "discussion_topics_update": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics.update"
    },
    "discussion_topics_destroy": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics.destroy"
    },
    "discussion_topics_reorder": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/reorder",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics.reorder"
    },
    "discussion_entries_update": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_entries.update"
    },
    "discussion_entries_destroy": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_entries.destroy"
    },
    "discussion_topics_api_show": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.show"
    },
    "discussion_topics_api_view": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/view",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.view"
    },
    "discussion_topics_api_add_entry": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.add_entry"
    },
    "discussion_topics_api_entries": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.entries"
    },
    "discussion_topics_api_add_reply": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.add_reply"
    },
    "discussion_topics_api_replies": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/replies",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.replies"
    },
    "discussion_topics_api_entry_list": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entry_list",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.entry_list"
    },
    "discussion_topics_api_mark_topic_read": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.mark_topic_read"
    },
    "discussion_topics_api_mark_topic_unread": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.mark_topic_unread"
    },
    "discussion_topics_api_mark_all_read": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.mark_all_read"
    },
    "discussion_topics_api_mark_all_unread": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/read_all",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.mark_all_unread"
    },
    "discussion_topics_api_mark_entry_read": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.mark_entry_read"
    },
    "discussion_topics_api_mark_entry_unread": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.mark_entry_unread"
    },
    "discussion_topics_api_rate_entry": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/entries/{entry_id}/rating",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.rate_entry"
    },
    "discussion_topics_api_subscribe_topic": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.subscribe_topic"
    },
    "discussion_topics_api_unsubscribe_topic": {
        "resource": "/api/v1/courses/{course_id}/discussion_topics/{topic_id}/subscribed",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.discussion_topics_api.unsubscribe_topic"
    },
    "terms_create": {
        "resource": "/api/v1/accounts/{account_id}/terms",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.terms.create"
    },
    "terms_update": {
        "resource": "/api/v1/accounts/{account_id}/terms/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.terms.update"
    },
    "terms_destroy": {
        "resource": "/api/v1/accounts/{account_id}/terms/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.terms.destroy"
    },
    "terms_api_index": {
        "resource": "/api/v1/accounts/{account_id}/terms",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.terms_api.index"
    },
    "enrollments_api_index": {
        "resource": "/api/v1/courses/{course_id}/enrollments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.index"
    },
    "enrollments_api_show": {
        "resource": "/api/v1/accounts/{account_id}/enrollments/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.show"
    },
    "enrollments_api_create": {
        "resource": "/api/v1/courses/{course_id}/enrollments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.create"
    },
    "enrollments_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/enrollments/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.destroy"
    },
    "enrollments_api_accept": {
        "resource": "/api/v1/courses/{course_id}/enrollments/{id}/accept",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.accept"
    },
    "enrollments_api_reject": {
        "resource": "/api/v1/courses/{course_id}/enrollments/{id}/reject",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.reject"
    },
    "enrollments_api_reactivate": {
        "resource": "/api/v1/courses/{course_id}/enrollments/{id}/reactivate",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.reactivate"
    },
    "enrollments_api_last_attended": {
        "resource": "/api/v1/courses/{course_id}/users/{user_id}/last_attended",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.enrollments_api.last_attended"
    },
    "errors_create": {
        "resource": "/api/v1/error_reports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.errors.create"
    },
    "external_tools_index": {
        "resource": "/api/v1/courses/{course_id}/external_tools",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_tools.index"
    },
    "external_tools_generate_sessionless_launch": {
        "resource": "/api/v1/courses/{course_id}/external_tools/sessionless_launch",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_tools.generate_sessionless_launch"
    },
    "external_tools_show": {
        "resource": "/api/v1/courses/{course_id}/external_tools/{external_tool_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_tools.show"
    },
    "external_tools_create": {
        "resource": "/api/v1/courses/{course_id}/external_tools",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_tools.create"
    },
    "external_tools_update": {
        "resource": "/api/v1/courses/{course_id}/external_tools/{external_tool_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_tools.update"
    },
    "external_tools_destroy": {
        "resource": "/api/v1/courses/{course_id}/external_tools/{external_tool_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.external_tools.destroy"
    },
    "favorites_list_favorite_courses": {
        "resource": "/api/v1/users/self/favorites/courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.list_favorite_courses"
    },
    "favorites_list_favorite_groups": {
        "resource": "/api/v1/users/self/favorites/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.list_favorite_groups"
    },
    "favorites_add_favorite_course": {
        "resource": "/api/v1/users/self/favorites/courses/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.add_favorite_course"
    },
    "favorites_add_favorite_groups": {
        "resource": "/api/v1/users/self/favorites/groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.add_favorite_groups"
    },
    "favorites_remove_favorite_course": {
        "resource": "/api/v1/users/self/favorites/courses/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.remove_favorite_course"
    },
    "favorites_remove_favorite_groups": {
        "resource": "/api/v1/users/self/favorites/groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.remove_favorite_groups"
    },
    "favorites_reset_course_favorites": {
        "resource": "/api/v1/users/self/favorites/courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.reset_course_favorites"
    },
    "favorites_reset_groups_favorites": {
        "resource": "/api/v1/users/self/favorites/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.favorites.reset_groups_favorites"
    },
    "feature_flags_index": {
        "resource": "/api/v1/courses/{course_id}/features",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.feature_flags.index"
    },
    "feature_flags_enabled_features": {
        "resource": "/api/v1/courses/{course_id}/features/enabled",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.feature_flags.enabled_features"
    },
    "feature_flags_show": {
        "resource": "/api/v1/courses/{course_id}/features/flags/{feature}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.feature_flags.show"
    },
    "feature_flags_update": {
        "resource": "/api/v1/courses/{course_id}/features/flags/{feature}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.feature_flags.update"
    },
    "feature_flags_delete": {
        "resource": "/api/v1/courses/{course_id}/features/flags/{feature}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.feature_flags.delete"
    },
    "files_api_quota": {
        "resource": "/api/v1/courses/{course_id}/files/quota",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.files.api_quota"
    },
    "files_api_index": {
        "resource": "/api/v1/courses/{course_id}/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.files.api_index"
    },
    "files_public_url": {
        "resource": "/api/v1/files/{id}/public_url",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.files.public_url"
    },
    "files_api_show": {
        "resource": "/api/v1/files/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.files.api_show"
    },
    "files_api_update": {
        "resource": "/api/v1/files/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.files.api_update"
    },
    "files_destroy": {
        "resource": "/api/v1/files/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.files.destroy"
    },
    "folders_api_index": {
        "resource": "/api/v1/folders/{id}/folders",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.api_index"
    },
    "folders_list_all_folders": {
        "resource": "/api/v1/courses/{course_id}/folders",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.list_all_folders"
    },
    "folders_resolve_path": {
        "resource": "/api/v1/courses/{course_id}/folders/by_path/*full_path",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.resolve_path"
    },
    "folders_show": {
        "resource": "/api/v1/courses/{course_id}/folders/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.show"
    },
    "folders_update": {
        "resource": "/api/v1/folders/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.update"
    },
    "folders_create": {
        "resource": "/api/v1/courses/{course_id}/folders",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.create"
    },
    "folders_api_destroy": {
        "resource": "/api/v1/folders/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.api_destroy"
    },
    "folders_create_file": {
        "resource": "/api/v1/folders/{folder_id}/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.create_file"
    },
    "folders_copy_file": {
        "resource": "/api/v1/folders/{dest_folder_id}/copy_file",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.copy_file"
    },
    "folders_copy_folder": {
        "resource": "/api/v1/folders/{dest_folder_id}/copy_folder",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.folders.copy_folder"
    },
    "usage_rights_set_usage_rights": {
        "resource": "/api/v1/courses/{course_id}/usage_rights",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.usage_rights.set_usage_rights"
    },
    "usage_rights_remove_usage_rights": {
        "resource": "/api/v1/courses/{course_id}/usage_rights",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.usage_rights.remove_usage_rights"
    },
    "usage_rights_licenses": {
        "resource": "/api/v1/courses/{course_id}/content_licenses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.usage_rights.licenses"
    },
    "grade_change_audit_api_for_assignment": {
        "resource": "/api/v1/audit/grade_change/assignments/{assignment_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grade_change_audit_api.for_assignment"
    },
    "grade_change_audit_api_for_course": {
        "resource": "/api/v1/audit/grade_change/courses/{course_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grade_change_audit_api.for_course"
    },
    "grade_change_audit_api_for_student": {
        "resource": "/api/v1/audit/grade_change/students/{student_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grade_change_audit_api.for_student"
    },
    "grade_change_audit_api_for_grader": {
        "resource": "/api/v1/audit/grade_change/graders/{grader_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grade_change_audit_api.for_grader"
    },
    "gradebook_history_api_days": {
        "resource": "/api/v1/courses/{course_id}/gradebook_history/days",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.gradebook_history_api.days"
    },
    "gradebook_history_api_day_details": {
        "resource": "/api/v1/courses/{course_id}/gradebook_history/{date}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.gradebook_history_api.day_details"
    },
    "gradebook_history_api_submissions": {
        "resource": "/api/v1/courses/{course_id}/gradebook_history/{date}/graders/{grader_id}/assignments/{assignment_id}/submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.gradebook_history_api.submissions"
    },
    "gradebook_history_api_feed": {
        "resource": "/api/v1/courses/{course_id}/gradebook_history/feed",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.gradebook_history_api.feed"
    },
    "grading_periods_index": {
        "resource": "/api/v1/accounts/{account_id}/grading_periods",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grading_periods.index"
    },
    "grading_periods_show": {
        "resource": "/api/v1/courses/{course_id}/grading_periods/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grading_periods.show"
    },
    "grading_periods_update": {
        "resource": "/api/v1/courses/{course_id}/grading_periods/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grading_periods.update"
    },
    "grading_periods_destroy": {
        "resource": "/api/v1/courses/{course_id}/grading_periods/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grading_periods.destroy"
    },
    "grading_standards_api_create": {
        "resource": "/api/v1/accounts/{account_id}/grading_standards",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grading_standards_api.create"
    },
    "grading_standards_api_context_index": {
        "resource": "/api/v1/courses/{course_id}/grading_standards",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grading_standards_api.context_index"
    },
    "grading_standards_api_context_show": {
        "resource": "/api/v1/courses/{course_id}/grading_standards/{grading_standard_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.grading_standards_api.context_show"
    },
    "group_categories_index": {
        "resource": "/api/v1/accounts/{account_id}/group_categories",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.index"
    },
    "group_categories_show": {
        "resource": "/api/v1/group_categories/{group_category_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.show"
    },
    "group_categories_create": {
        "resource": "/api/v1/accounts/{account_id}/group_categories",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.create"
    },
    "group_categories_update": {
        "resource": "/api/v1/group_categories/{group_category_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.update"
    },
    "group_categories_destroy": {
        "resource": "/api/v1/group_categories/{group_category_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.destroy"
    },
    "group_categories_groups": {
        "resource": "/api/v1/group_categories/{group_category_id}/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.groups"
    },
    "group_categories_users": {
        "resource": "/api/v1/group_categories/{group_category_id}/users",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.users"
    },
    "group_categories_assign_unassigned_members": {
        "resource": "/api/v1/group_categories/{group_category_id}/assign_unassigned_members",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_categories.assign_unassigned_members"
    },
    "groups_index": {
        "resource": "/api/v1/users/self/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.index"
    },
    "groups_context_index": {
        "resource": "/api/v1/accounts/{account_id}/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.context_index"
    },
    "groups_show": {
        "resource": "/api/v1/groups/{group_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.show"
    },
    "groups_create": {
        "resource": "/api/v1/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.create"
    },
    "groups_update": {
        "resource": "/api/v1/groups/{group_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.update"
    },
    "groups_destroy": {
        "resource": "/api/v1/groups/{group_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.destroy"
    },
    "groups_invite": {
        "resource": "/api/v1/groups/{group_id}/invite",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.invite"
    },
    "groups_users": {
        "resource": "/api/v1/groups/{group_id}/users",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.users"
    },
    "groups_create_file": {
        "resource": "/api/v1/groups/{group_id}/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.create_file"
    },
    "groups_preview_html": {
        "resource": "/api/v1/groups/{group_id}/preview_html",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.preview_html"
    },
    "groups_activity_stream": {
        "resource": "/api/v1/groups/{group_id}/activity_stream",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.activity_stream"
    },
    "groups_activity_stream_summary": {
        "resource": "/api/v1/groups/{group_id}/activity_stream/summary",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.groups.activity_stream_summary"
    },
    "group_memberships_index": {
        "resource": "/api/v1/groups/{group_id}/memberships",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_memberships.index"
    },
    "group_memberships_show": {
        "resource": "/api/v1/groups/{group_id}/memberships/{membership_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_memberships.show"
    },
    "group_memberships_create": {
        "resource": "/api/v1/groups/{group_id}/memberships",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_memberships.create"
    },
    "group_memberships_update": {
        "resource": "/api/v1/groups/{group_id}/memberships/{membership_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_memberships.update"
    },
    "group_memberships_destroy": {
        "resource": "/api/v1/groups/{group_id}/memberships/{membership_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.group_memberships.destroy"
    },
    "jwts_create": {
        "resource": "/api/v1/jwts",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.jwts.create"
    },
    "jwts_refresh": {
        "resource": "/api/v1/jwts/refresh",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.jwts.refresh"
    },
    "late_policy_show": {
        "resource": "/api/v1/courses/{id}/late_policy",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.late_policy.show"
    },
    "late_policy_create": {
        "resource": "/api/v1/courses/{id}/late_policy",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.late_policy.create"
    },
    "late_policy_update": {
        "resource": "/api/v1/courses/{id}/late_policy",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.late_policy.update"
    },
    "live_assessments/results_create": {
        "resource": "/api/v1/courses/{course_id}/live_assessments/{assessment_id}/results",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.live_assessments/results.create"
    },
    "live_assessments/results_index": {
        "resource": "/api/v1/courses/{course_id}/live_assessments/{assessment_id}/results",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.live_assessments/results.index"
    },
    "live_assessments/assessments_create": {
        "resource": "/api/v1/courses/{course_id}/live_assessments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.live_assessments/assessments.create"
    },
    "live_assessments/assessments_index": {
        "resource": "/api/v1/courses/{course_id}/live_assessments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.live_assessments/assessments.index"
    },
    "pseudonyms_index": {
        "resource": "/api/v1/accounts/{account_id}/logins",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.pseudonyms.index"
    },
    "pseudonyms_create": {
        "resource": "/api/v1/accounts/{account_id}/logins",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.pseudonyms.create"
    },
    "pseudonyms_update": {
        "resource": "/api/v1/accounts/{account_id}/logins/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.pseudonyms.update"
    },
    "pseudonyms_destroy": {
        "resource": "/api/v1/users/{user_id}/logins/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.pseudonyms.destroy"
    },
    "moderation_set_index": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.moderation_set.index"
    },
    "moderation_set_create": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.moderation_set.create"
    },
    "provisional_grades_status": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/status",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.provisional_grades.status"
    },
    "provisional_grades_select": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/select",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.provisional_grades.select"
    },
    "provisional_grades_copy_to_final_mark": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/copy_to_final_mark",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.provisional_grades.copy_to_final_mark"
    },
    "provisional_grades_publish": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/publish",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.provisional_grades.publish"
    },
    "context_modules_api_index": {
        "resource": "/api/v1/courses/{course_id}/modules",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_modules_api.index"
    },
    "context_modules_api_show": {
        "resource": "/api/v1/courses/{course_id}/modules/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_modules_api.show"
    },
    "context_modules_api_create": {
        "resource": "/api/v1/courses/{course_id}/modules",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_modules_api.create"
    },
    "context_modules_api_update": {
        "resource": "/api/v1/courses/{course_id}/modules/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_modules_api.update"
    },
    "context_modules_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/modules/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_modules_api.destroy"
    },
    "context_modules_api_relock": {
        "resource": "/api/v1/courses/{course_id}/modules/{id}/relock",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_modules_api.relock"
    },
    "context_module_items_api_index": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.index"
    },
    "context_module_items_api_show": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.show"
    },
    "context_module_items_api_create": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.create"
    },
    "context_module_items_api_update": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.update"
    },
    "context_module_items_api_select_mastery_path": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/select_mastery_path",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.select_mastery_path"
    },
    "context_module_items_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.destroy"
    },
    "context_module_items_api_mark_as_done": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/done",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.mark_as_done"
    },
    "context_module_items_api_item_sequence": {
        "resource": "/api/v1/courses/{course_id}/module_item_sequence",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.item_sequence"
    },
    "context_module_items_api_mark_item_read": {
        "resource": "/api/v1/courses/{course_id}/modules/{module_id}/items/{id}/mark_read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.context_module_items_api.mark_item_read"
    },
    "notification_preferences_index": {
        "resource": "/api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.notification_preferences.index"
    },
    "notification_preferences_category_index": {
        "resource": "/api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preference_categories",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.notification_preferences.category_index"
    },
    "notification_preferences_show": {
        "resource": "/api/v1/users/{user_id}/communication_channels/{communication_channel_id}/notification_preferences/{notification}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.notification_preferences.show"
    },
    "notification_preferences_update": {
        "resource": "/api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences/{notification}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.notification_preferences.update"
    },
    "notification_preferences_update_preferences_by_category": {
        "resource": "/api/v1/users/self/communication_channels/{communication_channel_id}/notification_preference_categories/{category}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.notification_preferences.update_preferences_by_category"
    },
    "notification_preferences_update_all": {
        "resource": "/api/v1/users/self/communication_channels/{communication_channel_id}/notification_preferences",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.notification_preferences.update_all"
    },
    "lti/originality_reports_api_create": {
        "resource": "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/originality_reports_api.create"
    },
    "lti/originality_reports_api_update": {
        "resource": "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/originality_reports_api.update"
    },
    "lti/originality_reports_api_show": {
        "resource": "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/originality_reports_api.show"
    },
    "outcome_groups_api_redirect": {
        "resource": "/api/v1/global/root_outcome_group",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.redirect"
    },
    "outcome_groups_api_index": {
        "resource": "/api/v1/accounts/{account_id}/outcome_groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.index"
    },
    "outcome_groups_api_link_index": {
        "resource": "/api/v1/accounts/{account_id}/outcome_group_links",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.link_index"
    },
    "outcome_groups_api_show": {
        "resource": "/api/v1/global/outcome_groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.show"
    },
    "outcome_groups_api_update": {
        "resource": "/api/v1/global/outcome_groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.update"
    },
    "outcome_groups_api_destroy": {
        "resource": "/api/v1/global/outcome_groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.destroy"
    },
    "outcome_groups_api_outcomes": {
        "resource": "/api/v1/global/outcome_groups/{id}/outcomes",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.outcomes"
    },
    "outcome_groups_api_link": {
        "resource": "/api/v1/global/outcome_groups/{id}/outcomes",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.link"
    },
    "outcome_groups_api_unlink": {
        "resource": "/api/v1/global/outcome_groups/{id}/outcomes/{outcome_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.unlink"
    },
    "outcome_groups_api_subgroups": {
        "resource": "/api/v1/global/outcome_groups/{id}/subgroups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.subgroups"
    },
    "outcome_groups_api_create": {
        "resource": "/api/v1/global/outcome_groups/{id}/subgroups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.create"
    },
    "outcome_groups_api_import": {
        "resource": "/api/v1/global/outcome_groups/{id}/import",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_groups_api.import"
    },
    "outcome_results_index": {
        "resource": "/api/v1/courses/{course_id}/outcome_results",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_results.index"
    },
    "outcome_results_rollups": {
        "resource": "/api/v1/courses/{course_id}/outcome_rollups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcome_results.rollups"
    },
    "outcomes_api_show": {
        "resource": "/api/v1/outcomes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcomes_api.show"
    },
    "outcomes_api_update": {
        "resource": "/api/v1/outcomes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.outcomes_api.update"
    },
    "wiki_pages_api_show_front_page": {
        "resource": "/api/v1/courses/{course_id}/front_page",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.show_front_page"
    },
    "wiki_pages_api_duplicate": {
        "resource": "/api/v1/courses/{course_id}/pages/{url}/duplicate",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.duplicate"
    },
    "wiki_pages_api_update_front_page": {
        "resource": "/api/v1/courses/{course_id}/front_page",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.update_front_page"
    },
    "wiki_pages_api_index": {
        "resource": "/api/v1/courses/{course_id}/pages",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.index"
    },
    "wiki_pages_api_create": {
        "resource": "/api/v1/courses/{course_id}/pages",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.create"
    },
    "wiki_pages_api_show": {
        "resource": "/api/v1/courses/{course_id}/pages/{url}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.show"
    },
    "wiki_pages_api_update": {
        "resource": "/api/v1/courses/{course_id}/pages/{url}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.update"
    },
    "wiki_pages_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/pages/{url}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.destroy"
    },
    "wiki_pages_api_revisions": {
        "resource": "/api/v1/courses/{course_id}/pages/{url}/revisions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.revisions"
    },
    "wiki_pages_api_show_revision": {
        "resource": "/api/v1/courses/{course_id}/pages/{url}/revisions/latest",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.show_revision"
    },
    "wiki_pages_api_revert": {
        "resource": "/api/v1/courses/{course_id}/pages/{url}/revisions/{revision_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.wiki_pages_api.revert"
    },
    "peer_reviews_api_index": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/peer_reviews",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.peer_reviews_api.index"
    },
    "peer_reviews_api_create": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.peer_reviews_api.create"
    },
    "peer_reviews_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.peer_reviews_api.destroy"
    },
    "lti/assignments_api_show": {
        "resource": "/api/lti/assignments/{assignment_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/assignments_api.show"
    },
    "lti/users_api_show": {
        "resource": "/api/lti/users/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/users_api.show"
    },
    "lti/users_api_group_index": {
        "resource": "/api/lti/groups/{group_id}/users",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/users_api.group_index"
    },
    "lti/submissions_api_show": {
        "resource": "/api/lti/assignments/{assignment_id}/submissions/{submission_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/submissions_api.show"
    },
    "lti/submissions_api_history": {
        "resource": "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/history",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/submissions_api.history"
    },
    "planner_notes_index": {
        "resource": "/api/v1/planner_notes",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_notes.index"
    },
    "planner_notes_show": {
        "resource": "/api/v1/planner_notes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_notes.show"
    },
    "planner_notes_update": {
        "resource": "/api/v1/planner_notes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_notes.update"
    },
    "planner_notes_create": {
        "resource": "/api/v1/planner_notes",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_notes.create"
    },
    "planner_notes_destroy": {
        "resource": "/api/v1/planner_notes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_notes.destroy"
    },
    "planner_overrides_items_index": {
        "resource": "/api/v1/planner/items",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_overrides.items_index"
    },
    "planner_overrides_index": {
        "resource": "/api/v1/planner/overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_overrides.index"
    },
    "planner_overrides_show": {
        "resource": "/api/v1/planner/overrides/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_overrides.show"
    },
    "planner_overrides_update": {
        "resource": "/api/v1/planner/overrides/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_overrides.update"
    },
    "planner_overrides_create": {
        "resource": "/api/v1/planner/overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_overrides.create"
    },
    "planner_overrides_destroy": {
        "resource": "/api/v1/planner/overrides/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.planner_overrides.destroy"
    },
    "polling/poll_sessions_index": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.index"
    },
    "polling/poll_sessions_show": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.show"
    },
    "polling/poll_sessions_create": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.create"
    },
    "polling/poll_sessions_update": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.update"
    },
    "polling/poll_sessions_destroy": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.destroy"
    },
    "polling/poll_sessions_open": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions/{id}/open",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.open"
    },
    "polling/poll_sessions_close": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions/{id}/close",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.close"
    },
    "polling/poll_sessions_opened": {
        "resource": "/api/v1/poll_sessions/opened",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.opened"
    },
    "polling/poll_sessions_closed": {
        "resource": "/api/v1/poll_sessions/closed",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_sessions.closed"
    },
    "polling/poll_choices_index": {
        "resource": "/api/v1/polls/{poll_id}/poll_choices",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_choices.index"
    },
    "polling/poll_choices_show": {
        "resource": "/api/v1/polls/{poll_id}/poll_choices/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_choices.show"
    },
    "polling/poll_choices_create": {
        "resource": "/api/v1/polls/{poll_id}/poll_choices",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_choices.create"
    },
    "polling/poll_choices_update": {
        "resource": "/api/v1/polls/{poll_id}/poll_choices/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_choices.update"
    },
    "polling/poll_choices_destroy": {
        "resource": "/api/v1/polls/{poll_id}/poll_choices/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_choices.destroy"
    },
    "polling/poll_submissions_show": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_submissions.show"
    },
    "polling/poll_submissions_create": {
        "resource": "/api/v1/polls/{poll_id}/poll_sessions/{poll_session_id}/poll_submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/poll_submissions.create"
    },
    "polling/polls_index": {
        "resource": "/api/v1/polls",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/polls.index"
    },
    "polling/polls_show": {
        "resource": "/api/v1/polls/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/polls.show"
    },
    "polling/polls_create": {
        "resource": "/api/v1/polls",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/polls.create"
    },
    "polling/polls_update": {
        "resource": "/api/v1/polls/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/polls.update"
    },
    "polling/polls_destroy": {
        "resource": "/api/v1/polls/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.polling/polls.destroy"
    },
    "progress_show": {
        "resource": "/api/v1/progress/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.progress.show"
    },
    "quizzes/quiz_assignment_overrides_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes/assignment_overrides",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_assignment_overrides.index"
    },
    "quizzes/quiz_extensions_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/extensions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_extensions.create"
    },
    "quizzes/quiz_ip_filters_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/ip_filters",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_ip_filters.index"
    },
    "quizzes/quiz_groups_show": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_groups.show"
    },
    "quizzes/quiz_groups_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_groups.create"
    },
    "quizzes/quiz_groups_update": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_groups.update"
    },
    "quizzes/quiz_groups_destroy": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_groups.destroy"
    },
    "quizzes/quiz_groups_reorder": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/groups/{id}/reorder",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_groups.reorder"
    },
    "quizzes/quiz_questions_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_questions.index"
    },
    "quizzes/quiz_questions_show": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_questions.show"
    },
    "quizzes/quiz_questions_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_questions.create"
    },
    "quizzes/quiz_questions_update": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_questions.update"
    },
    "quizzes/quiz_questions_destroy": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/questions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_questions.destroy"
    },
    "quizzes/quiz_reports_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_reports.index"
    },
    "quizzes/quiz_reports_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_reports.create"
    },
    "quizzes/quiz_reports_show": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_reports.show"
    },
    "quizzes/quiz_reports_abort": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/reports/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_reports.abort"
    },
    "quizzes/quiz_statistics_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/statistics",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_statistics.index"
    },
    "quizzes/quiz_submission_events_api_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_events_api.create"
    },
    "quizzes/quiz_submission_events_api_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/events",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_events_api.index"
    },
    "quizzes/quiz_submission_files_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/self/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_files.create"
    },
    "quizzes/quiz_submission_questions_index": {
        "resource": "/api/v1/quiz_submissions/{quiz_submission_id}/questions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_questions.index"
    },
    "quizzes/quiz_submission_questions_answer": {
        "resource": "/api/v1/quiz_submissions/{quiz_submission_id}/questions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_questions.answer"
    },
    "quizzes/quiz_submission_questions_flag": {
        "resource": "/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/flag",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_questions.flag"
    },
    "quizzes/quiz_submission_questions_unflag": {
        "resource": "/api/v1/quiz_submissions/{quiz_submission_id}/questions/{id}/unflag",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_questions.unflag"
    },
    "quizzes/quiz_submission_users_message": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{id}/submission_users/message",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submission_users.message"
    },
    "quizzes/quiz_submissions_api_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submissions_api.index"
    },
    "quizzes/quiz_submissions_api_submission": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submission",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submissions_api.submission"
    },
    "quizzes/quiz_submissions_api_show": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submissions_api.show"
    },
    "quizzes/quiz_submissions_api_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submissions_api.create"
    },
    "quizzes/quiz_submissions_api_update": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submissions_api.update"
    },
    "quizzes/quiz_submissions_api_complete": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/complete",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submissions_api.complete"
    },
    "quizzes/quiz_submissions_api_time": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{quiz_id}/submissions/{id}/time",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quiz_submissions_api.time"
    },
    "quizzes/quizzes_api_index": {
        "resource": "/api/v1/courses/{course_id}/quizzes",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quizzes_api.index"
    },
    "quizzes/quizzes_api_show": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quizzes_api.show"
    },
    "quizzes/quizzes_api_create": {
        "resource": "/api/v1/courses/{course_id}/quizzes",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quizzes_api.create"
    },
    "quizzes/quizzes_api_update": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quizzes_api.update"
    },
    "quizzes/quizzes_api_destroy": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quizzes_api.destroy"
    },
    "quizzes/quizzes_api_reorder": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{id}/reorder",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quizzes_api.reorder"
    },
    "quizzes/quizzes_api_validate_access_code": {
        "resource": "/api/v1/courses/{course_id}/quizzes/{id}/validate_access_code",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.quizzes/quizzes_api.validate_access_code"
    },
    "role_overrides_api_index": {
        "resource": "/api/v1/accounts/{account_id}/roles",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.role_overrides.api_index"
    },
    "role_overrides_show": {
        "resource": "/api/v1/accounts/{account_id}/roles/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.role_overrides.show"
    },
    "role_overrides_add_role": {
        "resource": "/api/v1/accounts/{account_id}/roles",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.role_overrides.add_role"
    },
    "role_overrides_remove_role": {
        "resource": "/api/v1/accounts/{account_id}/roles/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.role_overrides.remove_role"
    },
    "role_overrides_activate_role": {
        "resource": "/api/v1/accounts/{account_id}/roles/{id}/activate",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.role_overrides.activate_role"
    },
    "role_overrides_update": {
        "resource": "/api/v1/accounts/{account_id}/roles/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.role_overrides.update"
    },
    "rubrics_api_index": {
        "resource": "/api/v1/accounts/{account_id}/rubrics",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.rubrics_api.index"
    },
    "rubrics_api_show": {
        "resource": "/api/v1/accounts/{account_id}/rubrics/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.rubrics_api.show"
    },
    "sis_import_errors_api_index": {
        "resource": "/api/v1/accounts/{account_id}/sis_imports/{id}/errors",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sis_import_errors_api.index"
    },
    "sis_imports_api_index": {
        "resource": "/api/v1/accounts/{account_id}/sis_imports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sis_imports_api.index"
    },
    "sis_imports_api_create": {
        "resource": "/api/v1/accounts/{account_id}/sis_imports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sis_imports_api.create"
    },
    "sis_imports_api_show": {
        "resource": "/api/v1/accounts/{account_id}/sis_imports/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sis_imports_api.show"
    },
    "sis_imports_api_abort": {
        "resource": "/api/v1/accounts/{account_id}/sis_imports/{id}/abort",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sis_imports_api.abort"
    },
    "sis_imports_api_abort_all_pending": {
        "resource": "/api/v1/accounts/{account_id}/sis_imports/abort_all_pending",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sis_imports_api.abort_all_pending"
    },
    "sis_api_sis_assignments": {
        "resource": "/api/sis/accounts/{account_id}/assignments",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sis_api.sis_assignments"
    },
    "disable_post_to_sis_api_disable_post_to_sis": {
        "resource": "/api/sis/courses/{course_id}/disable_post_to_sis",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.disable_post_to_sis_api.disable_post_to_sis"
    },
    "search_recipients": {
        "resource": "/api/v1/conversations/find_recipients",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.search.recipients"
    },
    "search_all_courses": {
        "resource": "/api/v1/search/all_courses",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.search.all_courses"
    },
    "sections_index": {
        "resource": "/api/v1/courses/{course_id}/sections",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sections.index"
    },
    "sections_create": {
        "resource": "/api/v1/courses/{course_id}/sections",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sections.create"
    },
    "sections_crosslist": {
        "resource": "/api/v1/sections/{id}/crosslist/{new_course_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sections.crosslist"
    },
    "sections_uncrosslist": {
        "resource": "/api/v1/sections/{id}/crosslist",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sections.uncrosslist"
    },
    "sections_update": {
        "resource": "/api/v1/sections/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sections.update"
    },
    "sections_show": {
        "resource": "/api/v1/courses/{course_id}/sections/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sections.show"
    },
    "sections_destroy": {
        "resource": "/api/v1/sections/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.sections.destroy"
    },
    "services_api_show_kaltura_config": {
        "resource": "/api/v1/services/kaltura",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.services_api.show_kaltura_config"
    },
    "services_api_start_kaltura_session": {
        "resource": "/api/v1/services/kaltura_session",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.services_api.start_kaltura_session"
    },
    "shared_brand_configs_create": {
        "resource": "/api/v1/accounts/{account_id}/shared_brand_configs",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.shared_brand_configs.create"
    },
    "shared_brand_configs_update": {
        "resource": "/api/v1/accounts/{account_id}/shared_brand_configs/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.shared_brand_configs.update"
    },
    "shared_brand_configs_destroy": {
        "resource": "/api/v1/shared_brand_configs/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.shared_brand_configs.destroy"
    },
    "submission_comments_api_create_file": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submission_comments_api.create_file"
    },
    "submissions_create": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions.create"
    },
    "submissions_api_index": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.index"
    },
    "submissions_api_for_students": {
        "resource": "/api/v1/courses/{course_id}/students/submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.for_students"
    },
    "submissions_api_show": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.show"
    },
    "submissions_api_create_file": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.create_file"
    },
    "submissions_api_update": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.update"
    },
    "submissions_api_gradeable_students": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.gradeable_students"
    },
    "submissions_api_multiple_gradeable_students": {
        "resource": "/api/v1/courses/{course_id}/assignments/gradeable_students",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.multiple_gradeable_students"
    },
    "submissions_api_bulk_update": {
        "resource": "/api/v1/courses/{course_id}/submissions/update_grades",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.bulk_update"
    },
    "submissions_api_mark_submission_read": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.mark_submission_read"
    },
    "submissions_api_mark_submission_unread": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.mark_submission_unread"
    },
    "submissions_api_submission_summary": {
        "resource": "/api/v1/courses/{course_id}/assignments/{assignment_id}/submission_summary",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.submissions_api.submission_summary"
    },
    "tabs_index": {
        "resource": "/api/v1/courses/{course_id}/tabs",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.tabs.index"
    },
    "tabs_update": {
        "resource": "/api/v1/courses/{course_id}/tabs/{tab_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.tabs.update"
    },
    "user_observees_index": {
        "resource": "/api/v1/users/{user_id}/observees",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.user_observees.index"
    },
    "user_observees_create": {
        "resource": "/api/v1/users/{user_id}/observees",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.user_observees.create"
    },
    "user_observees_show": {
        "resource": "/api/v1/users/{user_id}/observees/{observee_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.user_observees.show"
    },
    "user_observees_update": {
        "resource": "/api/v1/users/{user_id}/observees/{observee_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.user_observees.update"
    },
    "user_observees_destroy": {
        "resource": "/api/v1/users/{user_id}/observees/{observee_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.user_observees.destroy"
    },
    "users_index": {
        "resource": "/api/v1/accounts/{account_id}/users",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.index"
    },
    "users_activity_stream": {
        "resource": "/api/v1/users/self/activity_stream",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.activity_stream"
    },
    "users_activity_stream_summary": {
        "resource": "/api/v1/users/self/activity_stream/summary",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.activity_stream_summary"
    },
    "users_todo_items": {
        "resource": "/api/v1/users/self/todo",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.todo_items"
    },
    "users_upcoming_events": {
        "resource": "/api/v1/users/self/upcoming_events",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.upcoming_events"
    },
    "users_missing_submissions": {
        "resource": "/api/v1/users/{user_id}/missing_submissions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.missing_submissions"
    },
    "users_ignore_stream_item": {
        "resource": "/api/v1/users/self/activity_stream/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.ignore_stream_item"
    },
    "users_ignore_all_stream_items": {
        "resource": "/api/v1/users/self/activity_stream",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.ignore_all_stream_items"
    },
    "users_create_file": {
        "resource": "/api/v1/users/{user_id}/files",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.create_file"
    },
    "users_api_show": {
        "resource": "/api/v1/users/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.api_show"
    },
    "users_create": {
        "resource": "/api/v1/accounts/{account_id}/users",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.create"
    },
    "users_create_self_registered_user": {
        "resource": "/api/v1/accounts/{account_id}/self_registration",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.create_self_registered_user"
    },
    "users_settings": {
        "resource": "/api/v1/users/{id}/settings",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.settings"
    },
    "users_get_custom_colors": {
        "resource": "/api/v1/users/{id}/colors",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.get_custom_colors"
    },
    "users_get_custom_color": {
        "resource": "/api/v1/users/{id}/colors/{asset_string}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.get_custom_color"
    },
    "users_set_custom_color": {
        "resource": "/api/v1/users/{id}/colors/{asset_string}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.set_custom_color"
    },
    "users_get_dashboard_positions": {
        "resource": "/api/v1/users/{id}/dashboard_positions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.get_dashboard_positions"
    },
    "users_set_dashboard_positions": {
        "resource": "/api/v1/users/{id}/dashboard_positions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.set_dashboard_positions"
    },
    "users_update": {
        "resource": "/api/v1/users/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.update"
    },
    "users_merge_into": {
        "resource": "/api/v1/users/{id}/merge_into/{destination_user_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.merge_into"
    },
    "users_split": {
        "resource": "/api/v1/users/{id}/split",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.users.split"
    },
    "profile_settings": {
        "resource": "/api/v1/users/{user_id}/profile",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.profile.settings"
    },
    "profile_profile_pics": {
        "resource": "/api/v1/users/{user_id}/avatars",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.profile.profile_pics"
    },
    "page_views_index": {
        "resource": "/api/v1/users/{user_id}/page_views",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.page_views.index"
    },
    "custom_data_set_data": {
        "resource": "/api/v1/users/{user_id}/custom_data(/*scope)",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_data.set_data"
    },
    "custom_data_get_data": {
        "resource": "/api/v1/users/{user_id}/custom_data(/*scope)",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_data.get_data"
    },
    "custom_data_delete_data": {
        "resource": "/api/v1/users/{user_id}/custom_data(/*scope)",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.custom_data.delete_data"
    },
    "course_nicknames_index": {
        "resource": "/api/v1/users/self/course_nicknames",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.course_nicknames.index"
    },
    "course_nicknames_show": {
        "resource": "/api/v1/users/self/course_nicknames/{course_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.course_nicknames.show"
    },
    "course_nicknames_update": {
        "resource": "/api/v1/users/self/course_nicknames/{course_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.course_nicknames.update"
    },
    "course_nicknames_delete": {
        "resource": "/api/v1/users/self/course_nicknames/{course_id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.course_nicknames.delete"
    },
    "course_nicknames_clear": {
        "resource": "/api/v1/users/self/course_nicknames",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.course_nicknames.clear"
    },
    "lti/subscriptions_api_create": {
        "resource": "/api/lti/subscriptions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/subscriptions_api.create"
    },
    "lti/subscriptions_api_destroy": {
        "resource": "/api/lti/subscriptions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/subscriptions_api.destroy"
    },
    "lti/subscriptions_api_show": {
        "resource": "/api/lti/subscriptions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/subscriptions_api.show"
    },
    "lti/subscriptions_api_update": {
        "resource": "/api/lti/subscriptions/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/subscriptions_api.update"
    },
    "lti/subscriptions_api_index": {
        "resource": "/api/lti/subscriptions",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.lti/subscriptions_api.index"
    },
    "epub_exports_index": {
        "resource": "/api/v1/epub_exports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.epub_exports.index"
    },
    "epub_exports_create": {
        "resource": "/api/v1/courses/{course_id}/epub_exports",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.epub_exports.create"
    },
    "epub_exports_show": {
        "resource": "/api/v1/courses/{course_id}/epub_exports/{id}",
        "docs": "https://canvas.instructure.com/doc/api/all_resources.html#method.epub_exports.show"
    }
}
