# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clue.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nclue.proto\"\x0e\n\x0c\x45mptyMessage\"/\n\x0cRequestLogin\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"<\n\rResponseLogin\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\"?\n\x11RequestCohortList\x12\x0c\n\x04term\x18\x01 \x01(\t\x12\x0c\n\x04page\x18\x02 \x01(\x05\x12\x0e\n\x06length\x18\x03 \x01(\x05\"\x86\x01\n\nCohortInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0egenerated_time\x18\x03 \x01(\t\x12\x14\n\x0cperson_count\x18\x04 \x01(\x05\x12\x0c\n\x04\x64one\x18\x05 \x01(\t\x12\x13\n\x0bupdate_flag\x18\x06 \x01(\x05\x12\r\n\x05state\x18\x07 \x01(\x05\"6\n\x12ResponseCohortList\x12 \n\x0b\x63ohort_list\x18\x01 \x03(\x0b\x32\x0b.CohortInfo\"\'\n\x11ResponseTableList\x12\x12\n\ntable_list\x18\x01 \x03(\t\"(\n\x12RequestTableSchema\x12\x12\n\ntable_name\x18\x01 \x01(\t\"\x87\x01\n\x13ResponseTableSchema\x12\x0f\n\x07\x63olumns\x18\x01 \x03(\t\x12\x12\n\nint32_cols\x18\x02 \x03(\t\x12\x12\n\nint64_cols\x18\x03 \x03(\t\x12\x12\n\nfloat_cols\x18\x04 \x03(\t\x12\x10\n\x08str_cols\x18\x05 \x03(\t\x12\x11\n\tbool_cols\x18\x06 \x03(\t\"N\n\x12RequestCohortTable\x12\x11\n\tfetch_num\x18\x01 \x01(\x05\x12\x11\n\tcohort_id\x18\x02 \x01(\x05\x12\x12\n\ntable_name\x18\x03 \x01(\t\"\x1d\n\x0cInt32Wrapper\x12\r\n\x05value\x18\x01 \x01(\x05\"\x1d\n\x0cInt64Wrapper\x12\r\n\x05value\x18\x01 \x01(\x03\"\x1d\n\x0c\x46loatWrapper\x12\r\n\x05value\x18\x01 \x01(\x02\"\x1b\n\nStrWrapper\x12\r\n\x05value\x18\x01 \x01(\t\"\x1c\n\x0b\x42oolWrapper\x12\r\n\x05value\x18\x01 \x01(\x08\"\xbe\x01\n\tTableData\x12#\n\x0cint32_values\x18\x01 \x03(\x0b\x32\r.Int32Wrapper\x12#\n\x0cint64_values\x18\x02 \x03(\x0b\x32\r.Int64Wrapper\x12#\n\x0c\x66loat_values\x18\x03 \x03(\x0b\x32\r.FloatWrapper\x12\x1f\n\nstr_values\x18\x04 \x03(\x0b\x32\x0b.StrWrapper\x12!\n\x0b\x62ool_values\x18\x05 \x03(\x0b\x32\x0c.BoolWrapper\";\n\x13RequestCohortStream\x12\x11\n\tfetch_num\x18\x01 \x01(\x05\x12\x11\n\tcohort_id\x18\x02 \x01(\x05\"\xea\x03\n\nPersonInfo\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x19\n\x11gender_concept_id\x18\x02 \x01(\x05\x12\x15\n\ryear_of_birth\x18\x03 \x01(\x05\x12\x17\n\x0frace_concept_id\x18\x04 \x01(\x05\x12\x1c\n\x14\x65thnicity_concept_id\x18\x05 \x01(\x05\x12\x16\n\x0emonth_of_birth\x18\x06 \x01(\x05\x12\x14\n\x0c\x64\x61y_of_birth\x18\x07 \x01(\x05\x12\x16\n\x0e\x62irth_datetime\x18\x08 \x01(\t\x12\x13\n\x0blocation_id\x18\t \x01(\x05\x12\x13\n\x0bprovider_id\x18\n \x01(\x05\x12\x14\n\x0c\x63\x61re_site_id\x18\x0b \x01(\x05\x12\x1b\n\x13person_source_value\x18\x0c \x01(\t\x12\x1b\n\x13gender_source_value\x18\r \x01(\t\x12 \n\x18gender_source_concept_id\x18\x0e \x01(\x05\x12\x19\n\x11race_source_value\x18\x0f \x01(\t\x12\x1e\n\x16race_source_concept_id\x18\x10 \x01(\x05\x12\x1e\n\x16\x65thnicity_source_value\x18\x11 \x01(\t\x12#\n\x1b\x65thnicity_source_concept_id\x18\x12 \x01(\x05\"\xfb\x03\n\x17\x43onditionOccurrenceInfo\x12\x1f\n\x17\x63ondition_occurrence_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x1c\n\x14\x63ondition_concept_id\x18\x03 \x01(\x05\x12\x1c\n\x14\x63ondition_start_date\x18\x04 \x01(\t\x12!\n\x19\x63ondition_type_concept_id\x18\x05 \x01(\x05\x12 \n\x18\x63ondition_start_datetime\x18\x06 \x01(\t\x12\x1a\n\x12\x63ondition_end_date\x18\x07 \x01(\t\x12\x1e\n\x16\x63ondition_end_datetime\x18\x08 \x01(\t\x12#\n\x1b\x63ondition_status_concept_id\x18\t \x01(\x05\x12\x13\n\x0bstop_reason\x18\n \x01(\t\x12\x13\n\x0bprovider_id\x18\x0b \x01(\x05\x12\x1b\n\x13visit_occurrence_id\x18\x0c \x01(\x05\x12\x17\n\x0fvisit_detail_id\x18\r \x01(\x05\x12\x1e\n\x16\x63ondition_source_value\x18\x0e \x01(\t\x12#\n\x1b\x63ondition_source_concept_id\x18\x0f \x01(\x05\x12%\n\x1d\x63ondition_status_source_value\x18\x10 \x01(\t\"\xc0\x01\n\tDeathInfo\x12\x11\n\tperson_id\x18\x01 \x01(\x05\x12\x12\n\ndeath_date\x18\x02 \x01(\t\x12\x16\n\x0e\x64\x65\x61th_datetime\x18\x03 \x01(\t\x12\x1d\n\x15\x64\x65\x61th_type_concept_id\x18\x04 \x01(\x05\x12\x18\n\x10\x63\x61use_concept_id\x18\x05 \x01(\t\x12\x1a\n\x12\x63\x61use_source_value\x18\x06 \x01(\t\x12\x1f\n\x17\x63\x61use_source_concept_id\x18\x07 \x01(\x05\"\xc8\x03\n\x12\x44\x65viceExposureInfo\x12\x1a\n\x12\x64\x65vice_exposure_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x19\n\x11\x64\x65vice_concept_id\x18\x03 \x01(\x05\x12\"\n\x1a\x64\x65vice_exposure_start_date\x18\x04 \x01(\t\x12\x1e\n\x16\x64\x65vice_type_concept_id\x18\x05 \x01(\x05\x12&\n\x1e\x64\x65vice_exposure_start_datetime\x18\x06 \x01(\t\x12 \n\x18\x64\x65vice_exposure_end_date\x18\x07 \x01(\t\x12$\n\x1c\x64\x65vice_exposure_end_datetime\x18\x08 \x01(\t\x12\x18\n\x10unique_device_id\x18\t \x01(\t\x12\x10\n\x08quantity\x18\n \x01(\x05\x12\x13\n\x0bprovider_id\x18\x0b \x01(\x05\x12\x1b\n\x13visit_occurrence_id\x18\x0c \x01(\x05\x12\x17\n\x0fvisit_detail_id\x18\r \x01(\x05\x12\x1b\n\x13\x64\x65vice_source_value\x18\x0e \x01(\t\x12 \n\x18\x64\x65vice_source_concept_id\x18\x0f \x01(\x05\"\xe7\x04\n\x10\x44rugExposureInfo\x12\x18\n\x10\x64rug_exposure_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x17\n\x0f\x64rug_concept_id\x18\x03 \x01(\x05\x12 \n\x18\x64rug_exposure_start_date\x18\x04 \x01(\t\x12\x1e\n\x16\x64rug_exposure_end_date\x18\x05 \x01(\t\x12\x1c\n\x14\x64rug_type_concept_id\x18\x06 \x01(\x05\x12$\n\x1c\x64rug_exposure_start_datetime\x18\x07 \x01(\t\x12\"\n\x1a\x64rug_exposure_end_datetime\x18\x08 \x01(\t\x12\x19\n\x11verbatim_end_date\x18\t \x01(\t\x12\x13\n\x0bstop_reason\x18\n \x01(\t\x12\x0f\n\x07refills\x18\x0b \x01(\x05\x12\x10\n\x08quantity\x18\x0c \x01(\x02\x12\x13\n\x0b\x64\x61ys_supply\x18\r \x01(\x05\x12\x0b\n\x03sig\x18\x0e \x01(\t\x12\x18\n\x10route_concept_id\x18\x0f \x01(\x05\x12\x12\n\nlot_number\x18\x10 \x01(\t\x12\x13\n\x0bprovider_id\x18\x11 \x01(\x05\x12\x1b\n\x13visit_occurrence_id\x18\x12 \x01(\x05\x12\x17\n\x0fvisit_detail_id\x18\x13 \x01(\x05\x12\x19\n\x11\x64rug_source_value\x18\x14 \x01(\t\x12\x1e\n\x16\x64rug_source_concept_id\x18\x15 \x01(\x05\x12\x1a\n\x12route_source_value\x18\x16 \x01(\t\x12\x1e\n\x16\x64ose_unit_source_value\x18\x17 \x01(\t\"\xb1\x04\n\x0fMeasurementInfo\x12\x16\n\x0emeasurement_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x1e\n\x16measurement_concept_id\x18\x03 \x01(\x05\x12\x18\n\x10measurement_date\x18\x04 \x01(\t\x12#\n\x1bmeasurement_type_concept_id\x18\x05 \x01(\x05\x12\x1c\n\x14measurement_datetime\x18\x06 \x01(\t\x12\x18\n\x10measurement_time\x18\x07 \x01(\t\x12\x1b\n\x13operator_concept_id\x18\x08 \x01(\x05\x12\x17\n\x0fvalue_as_number\x18\t \x01(\x02\x12\x1b\n\x13value_as_concept_id\x18\n \x01(\x05\x12\x17\n\x0funit_concept_id\x18\x0b \x01(\x05\x12\x11\n\trange_low\x18\x0c \x01(\x02\x12\x12\n\nrange_high\x18\r \x01(\x02\x12\x13\n\x0bprovider_id\x18\x0e \x01(\x05\x12\x1b\n\x13visit_occurrence_id\x18\x0f \x01(\x05\x12\x17\n\x0fvisit_detail_id\x18\x10 \x01(\x05\x12 \n\x18measurement_source_value\x18\x11 \x01(\t\x12%\n\x1dmeasurement_source_concept_id\x18\x12 \x01(\x05\x12\x19\n\x11unit_source_value\x18\x13 \x01(\t\x12\x1a\n\x12value_source_value\x18\x14 \x01(\t\"\xb5\x01\n\x15ObservationPeriodInfo\x12\x1d\n\x15observation_period_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12%\n\x1dobservation_period_start_date\x18\x03 \x01(\t\x12#\n\x1bobservation_period_end_date\x18\x04 \x01(\t\x12\x1e\n\x16period_type_concept_id\x18\x05 \x01(\x05\"\x8e\x04\n\x0fObservationInfo\x12\x16\n\x0eobservation_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x1e\n\x16observation_concept_id\x18\x03 \x01(\x05\x12\x18\n\x10observation_date\x18\x04 \x01(\t\x12#\n\x1bobservation_type_concept_id\x18\x05 \x01(\x05\x12\x1c\n\x14observation_datetime\x18\x06 \x01(\t\x12\x17\n\x0fvalue_as_number\x18\x07 \x01(\x02\x12\x17\n\x0fvalue_as_string\x18\x08 \x01(\t\x12\x1b\n\x13value_as_concept_id\x18\t \x01(\x05\x12\x1c\n\x14qualifier_concept_id\x18\n \x01(\x05\x12\x17\n\x0funit_concept_id\x18\x0b \x01(\x05\x12\x13\n\x0bprovider_id\x18\x0c \x01(\x05\x12\x1b\n\x13visit_occurrence_id\x18\r \x01(\x05\x12\x17\n\x0fvisit_detail_id\x18\x0e \x01(\x05\x12 \n\x18observation_source_value\x18\x0f \x01(\t\x12%\n\x1dobservation_source_concept_id\x18\x10 \x01(\x05\x12\x19\n\x11unit_source_value\x18\x11 \x01(\t\x12\x1e\n\x16qualifier_source_value\x18\x12 \x01(\x05\"\xa0\x03\n\x17ProcedureOccurrenceInfo\x12\x1f\n\x17procedure_occurrence_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x1c\n\x14procedure_concept_id\x18\x03 \x01(\x05\x12\x16\n\x0eprocedure_date\x18\x04 \x01(\t\x12!\n\x19procedure_type_concept_id\x18\x05 \x01(\x05\x12\x1a\n\x12procedure_datetime\x18\x06 \x01(\t\x12\x1b\n\x13modifier_concept_id\x18\x07 \x01(\x05\x12\x10\n\x08quantity\x18\x08 \x01(\x05\x12\x13\n\x0bprovider_id\x18\t \x01(\x05\x12\x1b\n\x13visit_occurrence_id\x18\n \x01(\x05\x12\x17\n\x0fvisit_detail_id\x18\x0b \x01(\x05\x12\x1e\n\x16procedure_source_value\x18\x0c \x01(\t\x12#\n\x1bprocedure_source_concept_id\x18\r \x01(\x05\x12\x1d\n\x15modifier_source_value\x18\x0e \x01(\t\"\x82\x04\n\x13VisitOccurrenceInfo\x12\x1b\n\x13visit_occurrence_id\x18\x01 \x01(\x05\x12\x11\n\tperson_id\x18\x02 \x01(\x05\x12\x18\n\x10visit_concept_id\x18\x03 \x01(\x05\x12\x18\n\x10visit_start_date\x18\x04 \x01(\t\x12\x16\n\x0evisit_end_date\x18\x05 \x01(\t\x12\x1d\n\x15visit_type_concept_id\x18\x06 \x01(\x05\x12\x1c\n\x14visit_start_datetime\x18\x07 \x01(\t\x12\x1a\n\x12visit_end_datetime\x18\x08 \x01(\t\x12\x13\n\x0bprovider_id\x18\t \x01(\x05\x12\x14\n\x0c\x63\x61re_site_id\x18\n \x01(\x05\x12\x1a\n\x12visit_source_value\x18\x0b \x01(\t\x12\x1f\n\x17visit_source_concept_id\x18\x0c \x01(\x05\x12#\n\x1b\x61\x64mitting_source_concept_id\x18\r \x01(\x05\x12\x1e\n\x16\x61\x64mitting_source_value\x18\x0e \x01(\t\x12\x1f\n\x17\x64ischarge_to_concept_id\x18\x0f \x01(\x05\x12!\n\x19\x64ischarge_to_source_value\x18\x10 \x01(\t\x12%\n\x1dpreceding_visit_occurrence_id\x18\x11 \x01(\x05\"*\n\x11RequestComparison\x12\x15\n\rcomparison_id\x18\x01 \x01(\x05\"F\n\x14\x43omparisonCohortInfo\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x14\n\x0cperson_count\x18\x03 \x01(\x05\"t\n\x11\x43omparisonRowInfo\x12\x11\n\tcategory1\x18\x01 \x01(\t\x12\x11\n\tcategory2\x18\x02 \x01(\t\x12\x0e\n\x06values\x18\x03 \x03(\t\x12\x0f\n\x07p_value\x18\x04 \x01(\x02\x12\x18\n\x10p_value_is_group\x18\x05 \x01(\x08\"t\n\x12ResponseComparison\x12\x0c\n\x04name\x18\x01 \x01(\t\x12*\n\x0b\x63ohort_list\x18\x02 \x03(\x0b\x32\x15.ComparisonCohortInfo\x12$\n\x08row_list\x18\x03 \x03(\x0b\x32\x12.ComparisonRowInfo\"1\n\x14RequestIncidenceRate\x12\x19\n\x11incidence_rate_id\x18\x01 \x01(\x05\"\x94\x03\n\x1aIncidenceRateResultRowInfo\x12\x18\n\x10target_cohort_id\x18\x01 \x01(\x05\x12\x19\n\x11outcome_cohort_id\x18\x02 \x01(\x05\x12\"\n\x1atarget_cohort_person_count\x18\x03 \x01(\x05\x12\x14\n\x0cperson_count\x18\x04 \x01(\x05\x12\x15\n\rcases_outcome\x18\x05 \x01(\x05\x12\"\n\x1aproportion_per_100_persons\x18\x06 \x01(\x02\x12!\n\x19proportion_per_1k_persons\x18\x07 \x01(\x02\x12\"\n\x1aproportion_per_10k_persons\x18\x08 \x01(\x02\x12\x1a\n\x12time_at_risk_years\x18\t \x01(\x02\x12\"\n\x1arate_per_100_persons_years\x18\n \x01(\x02\x12!\n\x19rate_per_1k_persons_years\x18\x0b \x01(\x02\x12\"\n\x1arate_per_10k_persons_years\x18\x0c \x01(\x02\"L\n\x1bResponseIncidenceRateResult\x12-\n\x08row_list\x18\x01 \x03(\x0b\x32\x1b.IncidenceRateResultRowInfo\"J\n\x1aRequestIncidenceRateStream\x12\x11\n\tfetch_num\x18\x01 \x01(\x05\x12\x19\n\x11incidence_rate_id\x18\x02 \x01(\x05\"\x8d\x03\n\x14IncidenceRateRawInfo\x12\x18\n\x10target_cohort_id\x18\x01 \x01(\x05\x12\x19\n\x11outcome_cohort_id\x18\x02 \x01(\x05\x12\x11\n\tperson_id\x18\x03 \x01(\x05\x12\x10\n\x08person_n\x18\x04 \x01(\x05\x12\x18\n\x10prior_outcome_yn\x18\x05 \x01(\x05\x12\x1b\n\x13index_date_earliest\x18\x06 \x01(\t\x12\x19\n\x11index_date_latest\x18\x07 \x01(\t\x12\x16\n\x0etar_start_date\x18\x08 \x01(\t\x12\x14\n\x0ctar_end_date\x18\t \x01(\t\x12\x17\n\x0f\x63ohort_end_date\x18\n \x01(\t\x12#\n\x1bobservation_period_end_date\x18\x0b \x01(\t\x12\x12\n\ndeath_date\x18\x0c \x01(\t\x12\x13\n\x0b\x63\x65nsor_date\x18\r \x01(\t\x12\x12\n\no_min_date\x18\x0e \x01(\t\x12\x0e\n\x06o_time\x18\x0f \x01(\x05\x12\x10\n\x08o_status\x18\x10 \x01(\x05\x32\xa1\n\n\x04\x43LUE\x12,\n\tAuthLogin\x12\r.RequestLogin\x1a\x0e.ResponseLogin\"\x00\x12:\n\rGetCohortList\x12\x12.RequestCohortList\x1a\x13.ResponseCohortList\"\x00\x12\x39\n\x12GetCohortTableList\x12\r.EmptyMessage\x1a\x12.ResponseTableList\"\x00\x12\x43\n\x14GetCohortTableSchema\x12\x13.RequestTableSchema\x1a\x14.ResponseTableSchema\"\x00\x12\x37\n\x0eGetCohortTable\x12\x13.RequestCohortTable\x1a\n.TableData\"\x00(\x01\x30\x01\x12?\n\x14GetCohortPersonTable\x12\x14.RequestCohortStream\x1a\x0b.PersonInfo\"\x00(\x01\x30\x01\x12Y\n!GetCohortConditionOccurrenceTable\x12\x14.RequestCohortStream\x1a\x18.ConditionOccurrenceInfo\"\x00(\x01\x30\x01\x12=\n\x13GetCohortDeathTable\x12\x14.RequestCohortStream\x1a\n.DeathInfo\"\x00(\x01\x30\x01\x12O\n\x1cGetCohortDeviceExposureTable\x12\x14.RequestCohortStream\x1a\x13.DeviceExposureInfo\"\x00(\x01\x30\x01\x12K\n\x1aGetCohortDrugExposureTable\x12\x14.RequestCohortStream\x1a\x11.DrugExposureInfo\"\x00(\x01\x30\x01\x12I\n\x19GetCohortMeasurementTable\x12\x14.RequestCohortStream\x1a\x10.MeasurementInfo\"\x00(\x01\x30\x01\x12U\n\x1fGetCohortObservationPeriodTable\x12\x14.RequestCohortStream\x1a\x16.ObservationPeriodInfo\"\x00(\x01\x30\x01\x12I\n\x19GetCohortObservationTable\x12\x14.RequestCohortStream\x1a\x10.ObservationInfo\"\x00(\x01\x30\x01\x12Y\n!GetCohortProcedureOccurrenceTable\x12\x14.RequestCohortStream\x1a\x18.ProcedureOccurrenceInfo\"\x00(\x01\x30\x01\x12Q\n\x1dGetCohortVisitOccurrenceTable\x12\x14.RequestCohortStream\x1a\x14.VisitOccurrenceInfo\"\x00(\x01\x30\x01\x12@\n\x13GetCohortComparison\x12\x12.RequestComparison\x1a\x13.ResponseComparison\"\x00\x12O\n\x16GetIncidenceRateResult\x12\x15.RequestIncidenceRate\x1a\x1c.ResponseIncidenceRateResult\"\x00\x12O\n\x13GetIncidenceRateRaw\x12\x1b.RequestIncidenceRateStream\x1a\x15.IncidenceRateRawInfo\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clue_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYMESSAGE._serialized_start=14
  _EMPTYMESSAGE._serialized_end=28
  _REQUESTLOGIN._serialized_start=30
  _REQUESTLOGIN._serialized_end=77
  _RESPONSELOGIN._serialized_start=79
  _RESPONSELOGIN._serialized_end=139
  _REQUESTCOHORTLIST._serialized_start=141
  _REQUESTCOHORTLIST._serialized_end=204
  _COHORTINFO._serialized_start=207
  _COHORTINFO._serialized_end=341
  _RESPONSECOHORTLIST._serialized_start=343
  _RESPONSECOHORTLIST._serialized_end=397
  _RESPONSETABLELIST._serialized_start=399
  _RESPONSETABLELIST._serialized_end=438
  _REQUESTTABLESCHEMA._serialized_start=440
  _REQUESTTABLESCHEMA._serialized_end=480
  _RESPONSETABLESCHEMA._serialized_start=483
  _RESPONSETABLESCHEMA._serialized_end=618
  _REQUESTCOHORTTABLE._serialized_start=620
  _REQUESTCOHORTTABLE._serialized_end=698
  _INT32WRAPPER._serialized_start=700
  _INT32WRAPPER._serialized_end=729
  _INT64WRAPPER._serialized_start=731
  _INT64WRAPPER._serialized_end=760
  _FLOATWRAPPER._serialized_start=762
  _FLOATWRAPPER._serialized_end=791
  _STRWRAPPER._serialized_start=793
  _STRWRAPPER._serialized_end=820
  _BOOLWRAPPER._serialized_start=822
  _BOOLWRAPPER._serialized_end=850
  _TABLEDATA._serialized_start=853
  _TABLEDATA._serialized_end=1043
  _REQUESTCOHORTSTREAM._serialized_start=1045
  _REQUESTCOHORTSTREAM._serialized_end=1104
  _PERSONINFO._serialized_start=1107
  _PERSONINFO._serialized_end=1597
  _CONDITIONOCCURRENCEINFO._serialized_start=1600
  _CONDITIONOCCURRENCEINFO._serialized_end=2107
  _DEATHINFO._serialized_start=2110
  _DEATHINFO._serialized_end=2302
  _DEVICEEXPOSUREINFO._serialized_start=2305
  _DEVICEEXPOSUREINFO._serialized_end=2761
  _DRUGEXPOSUREINFO._serialized_start=2764
  _DRUGEXPOSUREINFO._serialized_end=3379
  _MEASUREMENTINFO._serialized_start=3382
  _MEASUREMENTINFO._serialized_end=3943
  _OBSERVATIONPERIODINFO._serialized_start=3946
  _OBSERVATIONPERIODINFO._serialized_end=4127
  _OBSERVATIONINFO._serialized_start=4130
  _OBSERVATIONINFO._serialized_end=4656
  _PROCEDUREOCCURRENCEINFO._serialized_start=4659
  _PROCEDUREOCCURRENCEINFO._serialized_end=5075
  _VISITOCCURRENCEINFO._serialized_start=5078
  _VISITOCCURRENCEINFO._serialized_end=5592
  _REQUESTCOMPARISON._serialized_start=5594
  _REQUESTCOMPARISON._serialized_end=5636
  _COMPARISONCOHORTINFO._serialized_start=5638
  _COMPARISONCOHORTINFO._serialized_end=5708
  _COMPARISONROWINFO._serialized_start=5710
  _COMPARISONROWINFO._serialized_end=5826
  _RESPONSECOMPARISON._serialized_start=5828
  _RESPONSECOMPARISON._serialized_end=5944
  _REQUESTINCIDENCERATE._serialized_start=5946
  _REQUESTINCIDENCERATE._serialized_end=5995
  _INCIDENCERATERESULTROWINFO._serialized_start=5998
  _INCIDENCERATERESULTROWINFO._serialized_end=6402
  _RESPONSEINCIDENCERATERESULT._serialized_start=6404
  _RESPONSEINCIDENCERATERESULT._serialized_end=6480
  _REQUESTINCIDENCERATESTREAM._serialized_start=6482
  _REQUESTINCIDENCERATESTREAM._serialized_end=6556
  _INCIDENCERATERAWINFO._serialized_start=6559
  _INCIDENCERATERAWINFO._serialized_end=6956
  _CLUE._serialized_start=6959
  _CLUE._serialized_end=8272
# @@protoc_insertion_point(module_scope)
