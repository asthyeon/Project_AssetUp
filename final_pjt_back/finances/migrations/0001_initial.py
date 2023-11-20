from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('dcls_chrg_man', models.TextField()),
                ('homp_url', models.TextField()),
                ('cal_tel', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CreditLoanOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CreditLoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MortgageLoanOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MortgageLoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RentHouseLoanOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RentHouseLoanProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField(null=True)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField(choices=[(1, '제한 없음'), (2, '서민전용'), (3, '일부제한')])),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.bank')),
            ],
        ),
        migrations.CreateModel(
            name='SavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('rsrv_type_nm', models.TextField()),
                ('save_trm', models.IntegerField()),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.savingproduct')),
            ],
        ),
        migrations.CreateModel(
            name='DepositProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField(null=True)),
                ('mtrt_int', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('join_deny', models.IntegerField(choices=[(1, '제한 없음'), (2, '서민전용'), (3, '일부제한')])),
                ('join_member', models.TextField()),
                ('etc_note', models.TextField()),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.bank')),
            ],
        ),
        migrations.CreateModel(
            name='DepositOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField()),
                ('intr_rate2', models.FloatField()),
                ('save_trm', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.depositproduct')),
            ],
        ),
        migrations.CreateModel(
            name='BankOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_co_no', models.TextField()),
                ('area_cd', models.TextField()),
                ('area_nm', models.TextField()),
                ('exis_yn', models.BooleanField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.bank')),
            ],
        ),
        migrations.CreateModel(
            name='AnnuitySavingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField(null=True)),
                ('pnsn_kind', models.TextField()),
                ('pnsn_kind_nm', models.TextField()),
                ('sale_strt_day', models.TextField()),
                ('mntn_cnt', models.TextField()),
                ('prdt_type', models.TextField()),
                ('prdt_type_nm', models.TextField()),
                ('avg_prft_rate', models.FloatField()),
                ('dcls_rate', models.FloatField(null=True)),
                ('guar_rate', models.FloatField(null=True)),
                ('btrm_prft_rate_1', models.FloatField()),
                ('btrm_prft_rate_2', models.FloatField()),
                ('btrm_prft_rate_3', models.FloatField()),
                ('etc', models.TextField(null=True)),
                ('sale_co', models.TextField()),
                ('dcls_strt_day', models.TextField()),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField()),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.bank')),
            ],
        ),
        migrations.CreateModel(
            name='AnnuitySavingOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dcls_month', models.TextField()),
                ('fin_co_no', models.TextField()),
                ('fin_prdt_cd', models.TextField()),
                ('pnsn_recp_trm', models.TextField()),
                ('pnsn_recp_trm_nm', models.TextField()),
                ('pnsn_entr_age', models.TextField()),
                ('pnsn_entr_age_nm', models.TextField()),
                ('mon_paym_atm', models.TextField()),
                ('mon_paym_atm_nm', models.TextField()),
                ('paym_prd', models.TextField()),
                ('paym_prd_nm', models.TextField()),
                ('pnsn_strt_age', models.TextField()),
                ('pnsn_strt_age_nm', models.TextField()),
                ('pnsn_recp_amt', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finances.annuitysavingproduct')),
            ],
        ),
    ]
