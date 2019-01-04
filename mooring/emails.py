from io import BytesIO

from django.conf import settings

from mooring import pdf
from mooring.models import MooringsiteBooking, AdmissionsBooking, AdmissionsLine
from ledger.payments.pdf import create_invoice_pdf_bytes
from ledger.payments.models import Invoice

from ledger.emails.emails import EmailBase

default_from_email = settings.DEFAULT_FROM_EMAIL
default_campground_email = settings.CAMPGROUNDS_EMAIL
default_rottnest_email = settings.ROTTNEST_EMAIL

class TemplateEmailBase(EmailBase):
    subject = ''
    html_template = 'mooring/email/base_email.html'
    # txt_template can be None, in this case a 'tag-stripped' version of the html will be sent. (see send)
    txt_template = 'mooring/email/base_email.txt'


def send_admissions_booking_invoice(admissionsBooking):
    email_obj = TemplateEmailBase()
    admissionsLine = AdmissionsLine.objects.get(admissionsBooking=admissionsBooking)
    email_obj.subject = 'Admission fee payment invoice for {}'.format(admissionsLine.arrivalDate)
    email_obj.html_template = 'mooring/email/admissions_invoice.html'
    email_obj.txt_template = 'mooring/email/admissions_invoice.txt'
    email = admissionsBooking.customer.email

    context = {
        'booking': admissionsBooking,
        'arrivalDate': admissionsLine.arrivalDate
    }
    filename = 'invoice-{}({}).pdf'.format(admissionsLine.arrivalDate, admissionsBooking.customer.get_full_name())
    references = [b.invoice_reference for b in admissionsBooking.invoices.all()]
    invoice = Invoice.objects.filter(reference__in=references).order_by('-created')[0]
    invoice_pdf = create_invoice_pdf_bytes(filename,invoice)
    rottnest_email = default_rottnest_email
    email_obj.send([email], from_address=rottnest_email, context=context, attachments=[(filename, invoice_pdf, 'application/pdf')])


def send_booking_invoice(booking):
    email_obj = TemplateEmailBase()
    email_obj.subject = 'Your booking invoice for {}'.format(booking.mooringarea.name)
    email_obj.html_template = 'mooring/email/invoice.html'
    email_obj.txt_template = 'mooring/email/invoice.txt'

    email = booking.customer.email

    context = {
        'booking': booking
    }
    filename = 'invoice-{}({}-{}).pdf'.format(booking.mooringarea.name,booking.arrival,booking.departure)
    references = [b.invoice_reference for b in booking.invoices.all()]
    invoice = Invoice.objects.filter(reference__in=references).order_by('-created')[0]
        
    invoice_pdf = create_invoice_pdf_bytes(filename,invoice)

#    campground_email = booking.mooringarea.email if booking.mooringarea.email else default_campground_email
    campground_email = default_from_email 
    email_obj.send([email], from_address=campground_email, context=context, attachments=[(filename, invoice_pdf, 'application/pdf')])

def send_admissions_booking_confirmation(admissionsBooking, request):
    email_obj = TemplateEmailBase()
    admissionsLine = AdmissionsLine.objects.get(admissionsBooking=admissionsBooking)
    email_obj.subject = 'Admission Fee Payment Confirmation {} on {}'.format(admissionsBooking.confirmation_number,admissionsLine.arrivalDate)
    email_obj.html_template = 'mooring/email/admissions_confirmation.html'
    email_obj.txt_template = 'mooring/email/admissions_confirmation.txt'
    email = admissionsBooking.customer.email
    cc = None
    bcc = [default_rottnest_email]
    rottnest_email = default_rottnest_email
    my_bookings_url = request.build_absolute_uri('/mybookings/')

    context = {
        'booking': admissionsBooking,
        'my_bookings': my_bookings_url
    }
    att = BytesIO()
    pdf.create_admissions_confirmation(att, admissionsBooking)
    att.seek(0)
    filename = 'confirmation-AD{}({}).pdf'.format(admissionsBooking.id, admissionsBooking.customer.get_full_name())
    email_obj.send([email], from_address=rottnest_email, context=context, cc=cc, bcc=bcc, attachments=[(filename, att.read(), 'application/pdf')])

def send_booking_confirmation(booking,request):
    email_obj = TemplateEmailBase()
    email_obj.subject = 'Your booking {} at {} is confirmed'.format(booking.confirmation_number,booking.mooringarea.name)
    email_obj.html_template = 'mooring/email/confirmation.html'
    email_obj.txt_template = 'mooring/email/confirmation.txt'

    email = booking.customer.email

    cc = None
    bcc = [default_campground_email]

    #campground_email = booking.mooringarea.email if booking.mooringarea.email else default_campground_email
    campground_email = default_from_email
    if campground_email != default_campground_email:
        cc = [campground_email]

    my_bookings_url = request.build_absolute_uri('/mybookings/')
    booking_availability = request.build_absolute_uri('/availability/?site_id={}'.format(booking.mooringarea.id))
    unpaid_vehicle = False
    mobile_number = booking.customer.mobile_number
    booking_number = booking.details.get('phone',None)
    phone_number = booking.customer.phone_number
    tel = None
    if booking_number:
        tel = booking_number
    elif mobile_number:
        tel = mobile_number
    else:
        tel = phone_number
    tel = tel if tel else ''

    for v in booking.vehicle_payment_status:
        if v.get('Paid') == 'No':
            unpaid_vehicle = True
            break
    
    
    additional_info = booking.mooringarea.additional_info if booking.mooringarea.additional_info else ''

    msbs = MooringsiteBooking.objects.filter(booking=booking)
    contact_list = []
    moorings = []
    for m in msbs:
        if m.campsite.mooringarea not in moorings:
            moorings.append(m.campsite.mooringarea)
            contact = m.campsite.mooringarea.contact
            if not any(c['email'] == contact.email for c in contact_list) or not any(c['phone'] == contact.phone_number for c in contact_list):
                line = {'moorings': m.campsite.mooringarea.name, 'email': contact.email, 'phone': contact.phone_number}
                contact_list.append(line)
            else:
                index = next((index for (index, d) in enumerate(contact_list) if d['email'] == contact.email), None)
                contact_list[index]['moorings'] += ', ' + m.campsite.mooringarea.name


    
    context = {
        'booking': booking,
        'phone_number': tel,
        'campground_email': campground_email,
        'my_bookings': my_bookings_url,
        'availability': booking_availability,
        'unpaid_vehicle': unpaid_vehicle,
        'additional_info': additional_info,
        'contact_list': contact_list,
    }

    att = BytesIO()
    mooring_booking = []
    if MooringsiteBooking.objects.filter(booking=booking).count() > 0:
        mooring_booking = MooringsiteBooking.objects.filter(booking=booking)
    pdf.create_confirmation(att, booking, mooring_booking)
    att.seek(0)

    if booking.admission_payment:
        att2 = BytesIO()
        admissionsBooking = AdmissionsBooking.objects.get(id=booking.admission_payment.id)
        pdf.create_admissions_confirmation(att2, admissionsBooking)
        att2.seek(0)
        filename = 'confirmation-AD{}.pdf'.format(admissionsBooking.id)
        email_obj.send([email], from_address=campground_email, context=context, cc=cc, bcc=bcc, attachments=[('confirmation-PS{}.pdf'.format(booking.id), att.read(), 'application/pdf'), (filename, att2.read(), 'application/pdf')])
    else:
        email_obj.send([email], from_address=campground_email, context=context, cc=cc, bcc=bcc, attachments=[('confirmation-PS{}.pdf'.format(booking.id), att.read(), 'application/pdf')])
    booking.confirmation_sent = True
    booking.save()

def send_booking_cancelation(booking,request):
    email_obj = TemplateEmailBase()
    email_obj.subject = 'Cancelled: your booking {} at {},{}.'.format(booking.confirmation_number,booking.mooringarea.name,booking.mooringarea.park.name)
    email_obj.html_template = 'mooring/email/cancel.html'
    email_obj.txt_template = 'mooring/email/cancel.txt'

    email = booking.customer.email

    bcc = [default_campground_email]

    #campground_email = booking.mooringarea.email if booking.mooringarea.email else default_campground_email
    campground_email = default_from_email
    my_bookings_url = '{}mybookings/'.format(settings.PARKSTAY_EXTERNAL_URL)
    context = {
        'booking': booking,
        'my_bookings': my_bookings_url,
        'campground_email': campground_email
    }

    email_obj.send([email], from_address=campground_email, cc=[campground_email], bcc=bcc, context=context)

def send_booking_lapse(booking):
    email_obj = TemplateEmailBase()
    email_obj.subject = 'Your booking for {} has expired'.format(booking.campground.name)
    email_obj.html_template = 'mooring/email/lapse.html'
    email_obj.txt_template = 'mooring/email/lapse.txt'

    email = booking.customer.email

    context = {
        'booking': booking,
        'settings': settings,
    }
    email_obj.send([email], from_address=default_from_email, context=context)

