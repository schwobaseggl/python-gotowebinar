# -*- coding: utf-8 -*-
from dataclasses import dataclass, field, InitVar
from enum import Enum

from dataclasses_json import dataclass_json, config
from datetime import datetime
from typing import List


DateTimeField = field(metadata=config(
    encoder=datetime.isoformat,
    decoder=datetime.fromisoformat,
))


@dataclass_json
@dataclass(frozen=True)
class DateTimeRange:
    """
    A pair of DateTime values, the first of which serves as a start time and the second as an end time of an interval.
    """
    startTime: datetime = field(metadata=config(
        encoder=datetime.isoformat,
        decoder=datetime.fromisoformat,
    ))
    """The starting time of an interval, e.g. 2015-07-13T10:00:00Z"""
    endTime: datetime = field(metadata=config(
        encoder=datetime.isoformat,
        decoder=datetime.fromisoformat,
    ))
    """The ending time of an interval, e.g. 2015-07-13T22:00:00Z"""


@dataclass_json
@dataclass(frozen=True)
class EmailSettings:
    """Describes Confirmation email, Reminder email and Absentee follow-up email settings."""
    enabled: bool = True
    """Indicates whether email settings are enabled or disabled."""


@dataclass_json
@dataclass(frozen=True)
class AttendeeFollowUpEmailSetting(EmailSettings):
    """Describes Attendee follow-up email settings."""
    includeCertificate: bool = True
    """Indicates whether to include certificates in attendee follow-up emails is enabled or disabled."""


@dataclass_json
@dataclass(frozen=True)
class WebinarEmailSettings:
    confirmationEmail: EmailSettings = field(default_factory=EmailSettings)
    reminderEmail: EmailSettings = field(default_factory=EmailSettings)
    absenteeFollowUpEmail: EmailSettings = field(default_factory=EmailSettings)
    attendeeFollowUpEmail: AttendeeFollowUpEmailSetting = field(default_factory=AttendeeFollowUpEmailSetting)


@dataclass_json
@dataclass
class Webinar:
    subject: str  # The name/subject of the webinar (128 characters maximum)
    name: InitVar[str]  # subject in response: error in documentation (2019-09-23)
    times: List[DateTimeRange]  # Array with startTime and endTime for webinar. May be a singleton.
    webinarKey: str  # The unique key of the webinar
    webinarId: str  # The 9-digit webinar ID
    description: str  # A short description of the webinar
    organizerKey: str  # The key of the webinar organizer. Badly documented as int.
    organizerEmail: str  # The email of the webinar organizer
    organizerName: str  # The name of the webinar organizer
    accountKey: str  # The key of the account
    registrationUrl: str  # The URL the webinar invitees can use to register
    timeZone: str  # The timezone where the webinar is taking place, e.g.'Europe/Berlin'
    locale: str  # The webinar language:  "en_US", "de_DE", "es_ES", "fr_FR", "it_IT", or "zh_CN"
    inSession: bool = False  # Indicates whether there is a webinar session currently in progress
    impromptu: bool = False  # A boolean flag indicating if the webinar type is impromptu
    type: str = "single_session"  # Specifies the recurrence type:  "single_session", "series", or "sequence"
    numberOfRegistrants: int = 0  # The number of registrants at the webinar
    registrationLimit: int = 250  # The maximum number of registrants a webinar can have
    recurrencePeriod: str = "NEVER"  # Badly documented as "single_session", "series" or "sequence". BUT: "NEVER"
    isOndemand: bool = False  # A boolean flag indicating if the webinar should be ondemand
    experienceType: str = "CLASSIC"  # Badly documented. "classic", "broadcast" and "simulive".
    isPasswordProtected: bool = False  # A boolean flag indicating if the webinar is password protected

    # pendingRegistrants: int  # undocumented
    # deniedRegistrants: int  # undocumented
    # hasDisclaimer: bool  # undocumented
    # isMainOrganizerActive: bool  # undocumented
    # broadcast: bool  # undocumented
    # recordingAssetKey: str  # not supported, write only

    def __post_init__(self, name: str = None):
        self.subject = self.subject or name


@dataclass
class UpdateWebinar:
    """'subject', 'description', 'times', 'locale' 'timeZone', 'emailSetting'"""
    subject: str  # The name/subject of the webinar (128 characters maximum)
    description: str  # A short description of the webinar
    timeZone: str  # The timezone where the webinar is taking place, e.g.'Europe/Berlin'
    locale: str  # The webinar language:  "en_US", "de_DE", "es_ES", "fr_FR", "it_IT", or "zh_CN"
    times: List[DateTimeRange]  # Array with startTime and endTime for webinar. May be a singleton.
    emailSettings: WebinarEmailSettings = field(default_factory=WebinarEmailSettings)  # Describes email settings of a webinar.


@dataclass
class CreateWebinar:
    """'subject', 'description', 'times', 'locale' 'timeZone', 'emailSetting'"""
    subject: str  # The name/subject of the webinar (128 characters maximum)
    description: str  # A short description of the webinar
    timeZone: str  # The timezone where the webinar is taking place, e.g.'Europe/Berlin'
    locale: str  # The webinar language:  "en_US", "de_DE", "es_ES", "fr_FR", "it_IT", or "zh_CN"
    times: List[DateTimeRange]  # Array with startTime and endTime for webinar. May be a singleton.
    type: str = "single_session"  # Specifies the recurrence type:  "single_session", "series", or "sequence"
    emailSettings: WebinarEmailSettings = field(default_factory=WebinarEmailSettings)  # Describes email settings of a webinar.
    isOndemand: bool = False  # A boolean flag indicating if the webinar should be ondemand
    experienceType: str = "CLASSIC"  # Badly documented. "classic", "broadcast" and "simulive".