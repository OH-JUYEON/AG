from django.db import models

from AG.models import Period
# from campaign.models import CampaignHeader
# from donation.models import DonationHeader
# from funding.models import FundingHeader


# Create your models here.
class CityHeader(models.Model):
    city_name = models.CharField(null=False, max_length=10)
    city_image = models.ImageField(null=False, blank=False, upload_to='CityHeader/%Y/%m/%d')

    class Meta:
        db_table = "tbl_city_header"


class CityDetail(models.Model):
    city_header = models.ForeignKey(CityHeader, null=False, on_delete=models.CASCADE)
    city_detail_name = models.CharField(null=False, max_length=10)

    class Meta:
        db_table = "tbl_city_detail"


class SafeRegion(Period):
    city_header = models.ForeignKey(CityHeader, null=False, on_delete=models.CASCADE)
    safe_region_description = models.CharField(null=True, max_length=1024)
    safe_region_description2 = models.CharField(null=True, max_length=1024)
    safe_region_url = models.CharField(null=True, max_length=100)
    safe_region_info = models.CharField(null=True, max_length=1024)
    safe_region_content = models.CharField(null=True, max_length=10240)
    class Meta:
        db_table = "tbl_safe_region"


class SafetyScoreHeader(Period):
    city_header = models.ForeignKey(CityHeader, null=False, on_delete=models.CASCADE)
    strd_yr = models.CharField(null=True, max_length=4)
    pul = models.IntegerField(null=True)
    totl_zrmst = models.IntegerField(null=True)
    safety_score = models.IntegerField(null=True)

    class Meta:
        db_table = "tbl_safety_score_header"
#
#
# class SafetyScoreDetail(models.Model):
#     safety_score_detail_id = models.IntegerField(primary_key=True)
#     safety_score_header_id = models.ForeignKey(SafetyScoreHeader, null=False, on_delete=models.CASCADE)
#     city_detail_id = models.ForeignKey(CityDetail, null=False, on_delete=models.CASCADE)
#     adstrd = models.CharField(null=False, max_length=255)
#     plcst_nm = models.CharField(null=False, max_length=255)
#     sxcrm_zrmst = models.IntegerField(null=True)
#     mrdr_intsy_zrmst = models.IntegerField(null=True)
#     tfcrm_zrmst = models.IntegerField(null=True)
#     theft_zrmst = models.IntegerField(null=True)
#     incvlc_zrmst = models.IntegerField(null=True)
#     itecc_zrmst = models.IntegerField(null=True)
#     etc_zrmst = models.IntegerField(null=True)
#     totl_112 = models.IntegerField(null=True)
#     sxcrm_112 = models.IntegerField(null=True)
#     sxcrm_svlnc_112 = models.IntegerField(null=True)
#     sxcrm_dtvc_112 = models.IntegerField(null=True)
#     sxcrm_stkng_112 = models.IntegerField(null=True)
#     mrdr_intsy_112 = models.IntegerField(null=True)
#     mrdr_intsy_mrdr_112 = models.IntegerField(null=True)
#     mrdr_intsy_intsy_drug_112 = models.IntegerField(null=True)
#     tfcrm_112 = models.IntegerField(null=True)
#     tfcrm_tracc_112 = models.IntegerField(null=True)
#     tfcrm_tficv_112 = models.IntegerField(null=True)
#     tfcrm_tfvol_112 = models.IntegerField(null=True)
#     tfcrm_death_bgacd_112 = models.IntegerField(null=True)
#     tfcrm_rnwsl_112 = models.IntegerField(null=True)
#     tfcrm_drkdr_112 = models.IntegerField(null=True)
#     theft_112 = models.IntegerField(null=True)
#     theft_theft_112 = models.IntegerField(null=True)
#     theft_pckpk_112 = models.IntegerField(null=True)
#     itecc_112 = models.IntegerField(null=True)
#     itecc_fraud_112 = models.IntegerField(null=True)
#     itecc_vcphs_112 = models.IntegerField(null=True)
#     incvlc_112 = models.IntegerField(null=True)
#     incvlc_dstvc_112 = models.IntegerField(null=True)
#     incvlc_chlab_dmstc_112 = models.IntegerField(null=True)
#     incvlc_chlab_etc_112 = models.IntegerField(null=True)
#     incvlc_kncfm_112 = models.IntegerField(null=True)
#     incvlc_incvlc_112 = models.IntegerField(null=True)
#     incvlc_blsh_112 = models.IntegerField(null=True)
#     incvlc_thrt_112 = models.IntegerField(null=True)
#     incvlc_ptdmg_112 = models.IntegerField(null=True)
#     incvlc_schvo_112 = models.IntegerField(null=True)
#     incvlc_jvdiq_112 = models.IntegerField(null=True)
#     etc_112 = models.IntegerField(null=True)
#     etc_gmbln_112 = models.IntegerField(null=True)
#     etc_hsbrk_112 = models.IntegerField(null=True)
#     etc_bofet_112 = models.IntegerField(null=True)
#     etc_spprn_112 = models.IntegerField(null=True)
#     etc_etcrm_112 = models.IntegerField(null=True)
#     etc_frtln_112 = models.IntegerField(null=True)
#     etc_vonis_112 = models.IntegerField(null=True)
#     etc_jpbil_112 = models.IntegerField(null=True)
#     etc_odrls_112 = models.IntegerField(null=True)
#     etc_ptact_112 = models.IntegerField(null=True)
#     etc_prrsk_112 = models.IntegerField(null=True)
#     etc_emnof_112 = models.IntegerField(null=True)
#     etc_cntiq_112 = models.IntegerField(null=True)
#     etc_rackl_112 = models.IntegerField(null=True)
#     etc_emgbl_112 = models.IntegerField(null=True)
#     etc_secom_requst_112 = models.IntegerField(null=True)
#     etc_rnhm_112 = models.IntegerField(null=True)
#     etc_lopk_112 = models.IntegerField(null=True)
#     etc_ftx_112 = models.IntegerField(null=True)
#     etc_sucd_112 = models.IntegerField(null=True)
#     etc_msprn_112 = models.IntegerField(null=True)
#     etc_undtf_112 = models.IntegerField(null=True)
#     etc_fire_112 = models.IntegerField(null=True)
#     etc_rscrq_112 = models.IntegerField(null=True)
#     etc_noise_112 = models.IntegerField(null=True)
#     etc_stvnd_112 = models.IntegerField(null=True)
#     etc_etc_otins_112 = models.IntegerField(null=True)
#     etc_svcrq_112 = models.IntegerField(null=True)
#     etc_atgrl_112 = models.IntegerField(null=True)
#     etc_dsstr_112 = models.IntegerField(null=True)
#     etc_etc_dgram_112 = models.IntegerField(null=True)
#
#     class Meta:
#         db_table = "tbl_safety_score_detail"

#
# class SafetyScoreAction(Period):
#     safety_score_action_id = models.IntegerField(primary_key=True)
#     safety_score_header_id = models.ForeignKey(SafetyScoreHeader, null=False, on_delete=models.CASCADE)
#     campaign_header_id = models.ForeignKey(CampaignHeader, null=False, on_delete=models.CASCADE)
#     funding_header_id = models.ForeignKey(FundingHeader, null=False, on_delete=models.CASCADE)
#     donation_header_id = models.ForeignKey(DonationHeader, null=False, on_delete=models.CASCADE)
#     score = models.IntegerField(null=True)
#
#     class Meta:
#         db_table = "tbl_safety_score_action"

        
