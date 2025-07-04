import victron_mqtt
from victron_mqtt._victron_topics import topic_map
from victron_mqtt.constants import MetricKind


def test_settings_topics_present():
    assert "N/+/settings/0/Settings/CGwacs/Hub4Mode" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/Hub4Mode"].message_type is MetricKind.SELECT

    assert "N/+/settings/0/Settings/CGwacs/MaxFeedInPower" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/MaxFeedInPower"].message_type is MetricKind.NUMBER

    assert "N/+/settings/0/Settings/CGwacs/PreventFeedback" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/PreventFeedback"].message_type is MetricKind.SWITCH

    assert "N/+/settings/0/Settings/CGwacs/AcPowerSetpoint" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/AcPowerSetpoint"].message_type is MetricKind.NUMBER

    assert "N/+/settings/0/Settings/CGwacs/AcPowerSetpointPossible" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/AcPowerSetpointPossible"].message_type is MetricKind.SWITCH

    assert "N/+/settings/0/Settings/CGwacs/AcPowerSetpointReturnDelay" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/AcPowerSetpointReturnDelay"].message_type is MetricKind.NUMBER

    assert "N/+/settings/0/Settings/CGwacs/MaxChargePower" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/MaxChargePower"].message_type is MetricKind.NUMBER

    assert "N/+/settings/0/Settings/CGwacs/MaxDischargePower" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/MaxDischargePower"].message_type is MetricKind.NUMBER

    assert "N/+/settings/0/Settings/CGwacs/GridSetPoint" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/GridSetPoint"].message_type is MetricKind.NUMBER

    assert "N/+/settings/0/Settings/CGwacs/Sustain" in topic_map
    assert topic_map["N/+/settings/0/Settings/CGwacs/Sustain"].message_type is MetricKind.NUMBER

    assert "N/+/settings/0/Settings/Ess/Mode" in topic_map
    assert topic_map["N/+/settings/0/Settings/Ess/Mode"].message_type is MetricKind.SELECT

    assert "N/+/settings/0/Settings/Ess/MinimumSocLimit" in topic_map
    assert topic_map["N/+/settings/0/Settings/Ess/MinimumSocLimit"].message_type is MetricKind.NUMBER


def test_ess_mode_enum():
    assert hasattr(victron_mqtt, "EssMode")
