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
    msg.body = (
        f"A new initiate report was generated on {initiate.timestamp}:\r\n"
        f"Name: {initiate.name}\r\nPhone: {initiate.phone_number}\r\n"
        f"Problem: {initiate.initiate_problem}"
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
        f"A new registration request was generated on {surgeon.timestamp}:\r\n"
        f"Name: {surgeon.name}\r\nPhone: {surgeon.phone_number}\r\nArea: {surgeon.area}"
    )
    response = mail.send(msg)
    return response


def email_report(report):
    msg = Message(
        "A new surgeon/school report has been created ",
        sender=MAIL_DEFAULT_SENDER,
        recipients=MAIL_RECIPIENTS,
    )
    reporter_name = (
        report.opt_name
        if report.opt_name not in [None, "None", ""]
        else "no name given"
    )
    msg.body = (
        f"A new surgeon / school report was submitted on: {report.timestamp}\r\n"
        f"Reporter Name: {reporter_name}\r\n"
        f"Phone: {report.phone_number}\r\nSurgeon's Name: {report.surgeons_name}\r\n"
        f"Area: {report.area}\r\nProblem: {report.report_problem}"
    )

    response = mail.send(msg)
    return response
