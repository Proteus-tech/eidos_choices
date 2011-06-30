#!/usr/bin/env python
from django.utils.translation import ugettext_lazy as _

DEVELOPMENT_IN_PROGRESS = 1
READY_FOR_TESTING = 2
TESTING_IN_PROGRESS = 3
COMPLETED = 4

STORY_STATUS_CHOICES = (
    (DEVELOPMENT_IN_PROGRESS, _('Development In Progress')),
    (READY_FOR_TESTING, _('Ready For Testing')),
    (TESTING_IN_PROGRESS, _('Testing In Progress')),
    (COMPLETED, _('Completed')),
)


STORY_VISIBILITY_SHOWN = 1
STORY_VISIBILITY_HIDE_FROM_MOVED = 2
STORY_VISIBILITY_HIDE_FROM_DELETED = 3

STORY_VISIBILITY_CHOICES = (
    (STORY_VISIBILITY_SHOWN, _('Shown')),
    (STORY_VISIBILITY_HIDE_FROM_MOVED, _('Hidden (Moved)')),
    (STORY_VISIBILITY_HIDE_FROM_DELETED, _('Hidden (Deleted)')),
)