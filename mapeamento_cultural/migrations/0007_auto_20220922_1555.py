# Generated by Django 3.2.15 on 2022-09-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapeamento_cultural', '0006_auto_20220922_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artista',
            name='certidao_negativa_debitos_relativos_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='certidao_negativa_debitos_trabalhistas_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='certidao_negativa_debitos_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='certidao_regularidade_icms_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='certidao_regularidade_iss_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='certidao_regularidade_situacao_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='documento_empresario_exclusivo_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='file_cnpj_validade',
        ),
        migrations.RemoveField(
            model_name='artista',
            name='prova_inscricao_PJ_nacional_validade',
        ),
        migrations.AddField(
            model_name='artista',
            name='comprovante_de_cc_validade',
            field=models.DateField(blank=True, null=True, verbose_name='Comprovante de número de conta corrente (banco, agência e nº da conta)'),
        ),
        migrations.AddField(
            model_name='artista',
            name='comprovante_iss_validade',
            field=models.DateField(blank=True, null=True, verbose_name='Comprovante de inscrição do ISS Municipal'),
        ),
        migrations.AddField(
            model_name='artista',
            name='declaracao_n_viculo_validade',
            field=models.DateField(blank=True, null=True, verbose_name='Declaração de não vínculo com a Administração Federal, Estadual e Municipal'),
        ),
        migrations.AddField(
            model_name='artista',
            name='file_comprovante_residencia_validade',
            field=models.DateField(blank=True, null=True, verbose_name='Comprovante de residência'),
        ),
        migrations.AddField(
            model_name='artista',
            name='file_cpf_validade',
            field=models.DateField(blank=True, null=True, verbose_name='CPF'),
        ),
        migrations.AddField(
            model_name='artista',
            name='file_pis_validade',
            field=models.DateField(blank=True, null=True, verbose_name='PIS/PASEP/NIT'),
        ),
    ]
