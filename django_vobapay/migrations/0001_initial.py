# Generated by Django 2.2.28 on 2024-06-25 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VobapayTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('reference', models.TextField(null=True, verbose_name='reference')),
                ('backend_tx_id', models.TextField(null=True, verbose_name='backend tx id')),
                ('merchant_tx_id', models.CharField(max_length=255, unique=True, verbose_name='merchant tx id')),
                ('merchant_id', models.IntegerField(verbose_name='Merchant ID')),
                ('project_id', models.IntegerField(verbose_name='Project ID')),
                ('amount', models.PositiveIntegerField(verbose_name='amount in Cents')),
                ('currency', models.CharField(default='EUR', max_length=3, verbose_name='Currency Code (3 Chars)')),
                ('purpose', models.CharField(max_length=27, verbose_name='purpose')),
                ('redirect_url', models.TextField(verbose_name='redirect url')),
                ('notify_url', models.TextField(verbose_name='notify url')),
                ('success_url', models.TextField(verbose_name='success url')),
                ('error_url', models.TextField(verbose_name='error url')),
                ('payment_type', models.CharField(max_length=128, verbose_name='paymentname')),
                ('result_payment', models.IntegerField(null=True, verbose_name='return code from vobapay transaction')),
            ],
            options={
                'verbose_name': 'Vobapay Transaction',
                'verbose_name_plural': 'Vobapay Transactions',
            },
        ),
        migrations.CreateModel(
            name='VobapayResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('response_code', models.IntegerField(null=True, verbose_name='rc field from vobapay response')),
                ('response_msg', models.TextField(null=True, verbose_name='msg field from vobapay response')),
                ('raw_response', models.TextField(null=True, verbose_name='raw response')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responses', to='django_vobapay.VobapayTransaction')),
                ('request_data', models.TextField(blank=True, null=True, verbose_name='Request data')),
                ('request_url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Request url')),
            ],
            options={
                'verbose_name': 'Vobapay Response',
                'verbose_name_plural': 'Vobapay Responses',
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
