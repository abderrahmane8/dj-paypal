# Generated by Django 2.1.2 on 2018-10-01 11:51

from django.db import migrations

import djpaypal.fields


class Migration(migrations.Migration):

    dependencies = [
        ("djpaypal", "0005_auto_20180919_1447"),
    ]

    operations = [
        migrations.AddField(
            model_name="refund",
            name="refund_from_received_amount",
            field=djpaypal.fields.CurrencyAmountField(
                editable=False,
                help_text=(
                    "The currency and amount of the refund that is subtracted from the "
                    "original payment recipient's PayPal balance."
                ),
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="refund",
            name="refund_from_transaction_fee",
            field=djpaypal.fields.CurrencyAmountField(
                editable=False,
                help_text=(
                    "The currency and amount of the transaction fee that is refunded to "
                    "original the recipient of payment."
                ),
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="refund",
            name="total_refunded_amount",
            field=djpaypal.fields.CurrencyAmountField(
                editable=False,
                help_text=(
                    "The currency and amount of the total refund from the original "
                    "purchase."
                ),
                null=True,
            ),
        ),
    ]