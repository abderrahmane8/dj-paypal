# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 01:27
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import djpaypal.fields
import djpaypal.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAgreement',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=128)),
                ('state', models.CharField(choices=[('Active', 'Active'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('Created', 'Created'), ('Pending', 'Pending'), ('Reactivated', 'Reactivated'), ('Suspended', 'Suspended')], editable=False, max_length=128)),
                ('description', models.CharField(max_length=128)),
                ('start_date', models.DateTimeField(db_index=True)),
                ('agreement_details', django.contrib.postgres.fields.jsonb.JSONField()),
                ('payer', django.contrib.postgres.fields.jsonb.JSONField()),
                ('shipping_address', django.contrib.postgres.fields.jsonb.JSONField()),
                ('override_merchant_preferences', django.contrib.postgres.fields.jsonb.JSONField(default={}, blank=True)),
                ('override_charge_mode', django.contrib.postgres.fields.jsonb.JSONField(default={}, blank=True)),
                ('plan', django.contrib.postgres.fields.jsonb.JSONField()),
                ('merchant', django.contrib.postgres.fields.jsonb.JSONField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BillingPlan',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=127)),
                ('type', models.CharField(choices=[('FIXED', 'Fixed'), ('INFINITE', 'Infinite')], max_length=20)),
                ('state', models.CharField(choices=[('ACTIVE', 'Active'), ('CREATED', 'Created'), ('DELETED', 'Deleted'), ('INACTIVE', 'Inactive')], max_length=20)),
                ('create_time', models.DateTimeField(db_index=True, editable=False)),
                ('update_time', models.DateTimeField(db_index=True, editable=False)),
                ('merchant_preferences', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChargeModel',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('SHIPPING', 'Shipping'), ('TAX', 'Tax')], max_length=20)),
                ('amount', djpaypal.fields.CurrencyAmountField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Dispute',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('create_time', models.DateTimeField(db_index=True, editable=False)),
                ('update_time', models.DateTimeField(blank=True, db_index=True, editable=False, null=True)),
                ('disputed_transactions', django.contrib.postgres.fields.jsonb.JSONField(editable=False)),
                ('reason', models.CharField(choices=[('CANCELED_RECURRING_BILLING', 'Canceled recurring billing'), ('CREDIT_NOT_PROCESSED', 'Credit not processed'), ('DUPLICATE_TRANSACTION', 'Duplicate transaction'), ('INCORRECT_AMOUNT', 'Incorrect amount'), ('MERCHANDISE_OR_SERVICE_NOT_AS_DESCRIBED', 'Merchandise or service not as described'), ('MERCHANDISE_OR_SERVICE_NOT_RECEIVED', 'Merchandise or service not received'), ('OTHER', 'Other'), ('PAYMENT_BY_OTHER_MEANS', 'Payment by other means'), ('UNAUTHORISED', 'Unauthorized')], editable=False, max_length=39)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('OTHER', 'Other'), ('RESOLVED', 'Resolved'), ('UNDER_REVIEW', 'Under review'), ('WAITING_FOR_BUYER_RESPONSE', 'Waiting for buyer response'), ('WAITING_FOR_SELLER_RESPONSE', 'Waiting for seller response')], max_length=27)),
                ('dispute_amount', djpaypal.fields.CurrencyAmountField(editable=False)),
                ('dispute_outcome', django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True)),
                ('messages', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('seller_response_due_date', models.DateTimeField(blank=True, editable=False, null=True)),
                ('dispute_flow', models.CharField(choices=[('ACCOUNT_ISSUES', 'Account issues'), ('ACH_RETURNS', 'ACH returns'), ('ADMIN_FRAUD_REVERSAL', 'Admin fraud reversal'), ('BILLING', 'Billing'), ('CHARGEBACKS', 'Chargebacks'), ('COMPLAINT_RESOLUTION', 'Complaint resolution'), ('CORRECTION', 'Correction'), ('DEBIT_CARD_CHARGEBACK', 'Debit card chargeback'), ('FAX_ROUTING', 'Fax routing'), ('MIPS_COMPLAINT', 'MIPS complaint'), ('MIPS_COMPLAINT_ITEM', 'MIPS complaint item'), ('OPS_VERIFICATION_FLOW', 'OPS verification flow'), ('OTHER', 'Other'), ('PAYPAL_DISPUTE_RESOLUTION', 'Paypal dispute resolution'), ('PINLESS_DEBIT_RETURN', 'Pinless debit return'), ('PRICING_ADJUSTMENT', 'Pricing adjustment'), ('SPOOF_UNAUTH_CHILD', 'Spoof Unauth Child'), ('SPOOF_UNAUTH_PARENT', 'Spoof Unauth Parent'), ('THIRD_PARTY_CLAIM', 'Third party claim'), ('THIRD_PARTY_DISPUTE', 'Third party dispute'), ('TICKET_RETRIEVAL', 'Ticket retrieval'), ('UK_EXPRESS_RETURNS', 'UK Express returns'), ('UNKNOWN_FAXES', 'Unknown faxes'), ('VETTING', 'Vetting')], editable=False, max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('first_name', models.CharField(db_index=True, max_length=64)),
                ('last_name', models.CharField(db_index=True, max_length=64)),
                ('email', models.CharField(db_index=True, max_length=127)),
                ('shipping_address', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, help_text='The most recent Django user that transacted as this Payer (best-effort).', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paypal_payers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('intent', models.CharField(choices=[('authorize', 'Authorize'), ('order', 'Order'), ('sale', 'Sale')], max_length=9)),
                ('cart', models.CharField(blank=True, db_index=True, max_length=127, null=True)),
                ('payer', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('transactions', django.contrib.postgres.fields.jsonb.JSONField()),
                ('state', models.CharField(choices=[('approved', 'Approved'), ('created', 'Created'), ('failed', 'Failed')], max_length=8)),
                ('experience_profile_id', models.CharField(db_index=True, max_length=127)),
                ('note_to_payer', models.CharField(max_length=165)),
                ('create_time', models.DateTimeField(db_index=True, editable=False)),
                ('update_time', models.DateTimeField(db_index=True, editable=False)),
                ('redirect_urls', django.contrib.postgres.fields.jsonb.JSONField()),
                ('failure_reason', models.CharField(choices=[('CANNOT_PAY_THIS_PAYEE', 'Cannot pay this payee'), ('INVALID_PAYMENT_METHOD', 'Invalid payment method'), ('PAYEE_FILTER_RESTRICTIONS', 'Payee filter restrictions'), ('PAYER_CANNOT_PAY', 'Payer cannot pay'), ('REDIRECT_REQUIRED', 'Redirect required'), ('UNABLE_TO_COMPLETE_TRANSACTION', 'Unable to complete transaction')], max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PaymentDefinition',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('type', models.CharField(choices=[('REGULAR', 'Regular'), ('TRIAL', 'Trial')], max_length=20)),
                ('frequency_interval', models.PositiveSmallIntegerField()),
                ('frequency', models.CharField(choices=[('DAY', 'Day'), ('MONTH', 'Month'), ('WEEK', 'Week'), ('YEAR', 'Year')], max_length=20)),
                ('cycles', models.PositiveSmallIntegerField()),
                ('amount', djpaypal.fields.CurrencyAmountField()),
                ('charge_models', models.ManyToManyField(to='djpaypal.ChargeModel')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PreparedBillingAgreement',
            fields=[
                ('id', models.CharField(editable=False, help_text='Same as the BillingAgreement token', max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('executed_at', models.DateTimeField(blank=True, null=True)),
                ('canceled_at', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('executed_agreement', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prepared_agreements', to='djpaypal.BillingAgreement')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refund',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('amount', djpaypal.fields.CurrencyAmountField(help_text='The refund amount. Includes both the amount refunded to the payer and amount of the fee refunded to the payee.')),
                ('state', models.CharField(choices=[('cancelled', 'Cancelled'), ('completed', 'Completed'), ('failed', 'Failed'), ('pending', 'Pending')], editable=False, help_text='The state of the refund.', max_length=9)),
                ('reason', models.TextField(blank=True, help_text='The reason that the transaction is being refunded.')),
                ('invoice_number', models.CharField(blank=True, help_text='Your own invoice or tracking ID number.', max_length=127)),
                ('description', models.TextField(blank=True, help_text='The refund description.')),
                ('create_time', models.DateTimeField(db_index=True, editable=False)),
                ('update_time', models.DateTimeField(db_index=True, editable=False)),
                ('reason_code', models.CharField(choices=[('ECHECK', 'eCheck')], editable=False, help_text='The reason code for the pending refund state.', max_length=6)),
                ('refund_reason_code', models.CharField(choices=[('ADJUSTMENT_REVERSAL', 'Adjustment reversal'), ('ADMIN_FRAUD_REVERSAL', 'Admin fraud reversal'), ('ADMIN_REVERSAL', 'Admin reversal'), ('APPEAL', 'Appeal'), ('BUYER_COMPLAINT', 'Buyer complaint'), ('CHARGEBACK', 'Chargeback'), ('CHARGEBACK_SETTLEMENT', 'Chargeback settlement'), ('DENIED', 'Denied'), ('DISPUTE_PAYOUT', 'Dispute payout'), ('FUNDING', 'Funding'), ('GUARANTEE', 'Guarantee'), ('LIMITS', 'Limits'), ('NO_FAULT', 'No fault'), ('OTHER', 'Other'), ('REFUND', 'Refund'), ('REGULATORY_BLOCK', 'Regulatory block'), ('REGULATORY_REJECT', 'Regulatory reject'), ('REGULATORY_REVIEW_EXCEEDING_SLA', 'Regulatory review exceeding SLA'), ('RISK', 'Risk'), ('SELLER_FAULT', 'Seller fault'), ('SELLER_VOLUNTARY', 'Seller voluntary'), ('THIRDPARTY_LOGISTICS_FAULT', 'Third-party logistics fault'), ('UNAUTH_CLAIM', 'Unauth claim'), ('UNAUTH_SPOOF', 'Unauth spoof')], editable=False, help_text='The PayPal-assigned reason codes for the refund.', max_length=31)),
                ('refund_funding_type', models.CharField(choices=[('PAYOUT', 'Payout')], editable=False, help_text="Indicates whether the refund amount is funded by the payee's funding account or another funding account.", max_length=6)),
                ('parent_payment', models.ForeignKey(editable=False, help_text='The payment on which this transaction is based', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='refunds', to='djpaypal.Payment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('amount', djpaypal.fields.CurrencyAmountField(editable=False)),
                ('payment_mode', models.CharField(choices=[('DELAYED_TRANSFER', 'Delayed transfer'), ('ECHECK', 'eCheck'), ('INSTANT_TRANSFER', 'Instant transfer'), ('MANUAL_BANK_TRANSFER', 'Manual bank transfer')], editable=False, max_length=20)),
                ('state', models.CharField(choices=[('completed', 'Completed'), ('denied', 'Denied'), ('partially_refunded', 'Partially refunded'), ('pending', 'Pending'), ('refunded', 'Refunded')], editable=False, max_length=20)),
                ('reason_code', models.CharField(choices=[('BUYER_COMPLAINT', 'Buyer complaint'), ('CHARGEBACK', 'Chargeback'), ('ECHECK', 'eCheck'), ('GUARANTEE', 'Guarantee'), ('INTERNATIONAL_WITHDRAWAL', 'International withdrawal'), ('PAYMENT_REVIEW', 'Payment review'), ('RECEIVING_PREFERENCE_MANDATES_MANUAL_ACTION', 'Receiving preference mandates manual action'), ('REFUND', 'Refund'), ('REGULATORY_REVIEW', 'Regulatory review'), ('TRANSACTION_APPROVED_AWAITING_FUNDING', 'Transaction approved awaiting funding'), ('UNCONFIRMED_SHIPPING_ADDRESS', 'Unconfirmed shipping address'), ('UNILATERAL', 'Unilateral'), ('VERIFICATION_REQUIRED', 'Verification required')], editable=False, max_length=43)),
                ('protection_eligibility', models.CharField(choices=[('ELIGIBLE', 'Eligible'), ('INELIGIBLE', 'Ineligible'), ('PARTIALLY_ELIGIBLE', 'Partially eligible')], editable=False, max_length=18)),
                ('protection_eligibility_type', models.CharField(choices=[('ITEM_NOT_RECEIVED_ELIGIBLE', 'Item not received eligible'), ('ITEM_NOT_RECEIVED_ELIGIBLE,UNAUTHORIZED_PAYMENT_ELIGIBLE', 'Both'), ('UNAUTHORIZED_PAYMENT_ELIGIBLE', 'Unauthorized payment eligible')], editable=False, max_length=56)),
                ('clearing_time', models.DateTimeField(blank=True, editable=False, null=True)),
                ('transaction_fee', djpaypal.fields.CurrencyAmountField(blank=True, editable=False, null=True)),
                ('receivable_amount', djpaypal.fields.CurrencyAmountField(blank=True, editable=False, null=True)),
                ('exchange_rate', models.CharField(editable=False, max_length=64)),
                ('fmf_details', django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True)),
                ('receipt_id', models.CharField(db_index=True, editable=False, max_length=19)),
                ('processor_response', django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True)),
                ('create_time', models.DateTimeField(db_index=True, editable=False)),
                ('update_time', models.DateTimeField(db_index=True, editable=False)),
                ('soft_descriptor', models.CharField(blank=True, editable=False, max_length=127)),
                ('billing_agreement', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='djpaypal.BillingAgreement')),
                ('parent_payment', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to='djpaypal.Payment')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WebhookEvent',
            fields=[
                ('id', models.CharField(editable=False, max_length=128, primary_key=True, serialize=False)),
                ('livemode', models.BooleanField()),
                ('djpaypal_created', models.DateTimeField(auto_now_add=True)),
                ('djpaypal_updated', models.DateTimeField(auto_now=True)),
                ('event_version', models.CharField(editable=False, max_length=8)),
                ('create_time', models.DateTimeField(db_index=True, editable=False)),
                ('event_type', models.CharField(editable=False, max_length=64)),
                ('resource_type', models.CharField(editable=False, max_length=64)),
                ('resource', django.contrib.postgres.fields.jsonb.JSONField(editable=False)),
                ('status', models.CharField(blank=True, editable=False, max_length=64)),
                ('summary', models.CharField(editable=False, max_length=256)),
                ('transmissions', django.contrib.postgres.fields.jsonb.JSONField(blank=True, editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WebhookEventTrigger',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('headers', django.contrib.postgres.fields.jsonb.JSONField()),
                ('body', models.TextField(blank=True)),
                ('valid', models.BooleanField(default=False)),
                ('processed', models.BooleanField(default=False)),
                ('exception', models.CharField(blank=True, max_length=128)),
                ('traceback', models.TextField(blank=True)),
                ('djpaypal_version', models.CharField(default=djpaypal.utils.get_version, help_text='The version of dj-paypal when the webhook was received', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('webhook_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djpaypal.WebhookEvent')),
            ],
        ),
        migrations.AddField(
            model_name='refund',
            name='sale',
            field=models.ForeignKey(editable=False, help_text='The sale transaction being refunded.', on_delete=django.db.models.deletion.PROTECT, related_name='refunds', to='djpaypal.Sale'),
        ),
        migrations.AddField(
            model_name='billingplan',
            name='payment_definitions',
            field=models.ManyToManyField(to='djpaypal.PaymentDefinition'),
        ),
        migrations.AddField(
            model_name='billingagreement',
            name='payer_model',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='djpaypal.Payer'),
        ),
        migrations.AddField(
            model_name='billingagreement',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
