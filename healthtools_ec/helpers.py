from flask_login import current_user
from flask_mail import Message

from .app import mail
from .config import MAIL_DEFAULT_SENDER, MAIL_RECIPIENTS


def body_tag_args():
    classes = []
    args = {}

    if current_user.is_authenticated:
        classes.append("loggedin")
        args["dataUserName"] = current_user.username
        # args['dataUserEmail'] = current_user.full_name
        args["dataUserId"] = current_user.id

    args["class_"] = " ".join(classes)
    return args


def email_initiates(initiate):
    msg = Message(
        "A new initiate is in trouble",
        sender=MAIL_DEFAULT_SENDER,
        recipients=MAIL_RECIPIENTS,
    )
    msg.body = "A new initiate report was generated on %s:\r\nName: %s\r\nPhone: %s\r\nProblem: %s" % (
        initiate.timestamp,
        initiate.name,
        initiate.phone_number,
        initiate.initiate_problem,
    )
    response = mail.send(msg)
    return response


def email_register(surgeon):
    msg = Message(
        "A new Surgeon has registered",
        sender=MAIL_DEFAULT_SENDER,
        recipients=MAIL_RECIPIENTS,
    )
    msg.body = (
        "A new registration request was generated on %s:\r\nName: %s\r\nPhone: %s\r\nArea: %s"
        % (surgeon.timestamp, surgeon.name, surgeon.phone_number, surgeon.area)
    )
    response = mail.send(msg)
    return response


def email_report(report):
    msg = Message(
        "A new surgeon/school report has been created ",
        sender=MAIL_DEFAULT_SENDER,
        recipients=MAIL_RECIPIENTS,
    )
    msg.body = "A new surgeon / school report was submitted on %s:\r\nReporter Name: %s\r\nPhone: \
            %s\r\nSurgeon's Name: %s\r\nArea: %s\r\nProblem: %s" % (
        report.timestamp,
        report.opt_name
        if report.opt_name not in [None, "None", ""]
        else "no name given",
        report.phone_number,
        report.surgeons_name,
        report.area,
        report.report_problem,
    )
    response = mail.send(msg)
    return response
