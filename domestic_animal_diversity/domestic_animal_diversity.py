# Auto generated from domestic_animal_diversity.yaml by pythongen.py version: 0.9.0
# Generation date: 2021-11-18T16:15:23
# Schema: example
#
# id: https://w3id.org/example
# description: example
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Datetime, Float, Integer, String
from linkml_runtime.utils.metamodelcore import XSDDateTime

metamodel_version = "1.7.0"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
EXAMPLE = CurieNamespace('example', 'https://w3id.org/example')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = EXAMPLE


# Types
class DAD-IS7.9.2021HttpIdentifier(String):
    type_class_uri = XSD.string
    type_class_curie = "xsd:string"
    type_name = "DAD-IS 7.9.2021 http identifier"
    type_model_uri = EXAMPLE["DAD-IS7.9.2021HttpIdentifier"]


# Class references



@dataclass
class Breed(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.Breed
    class_class_curie: ClassVar[str] = "example:Breed"
    class_name: ClassVar[str] = "Breed"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.Breed

    Country: Optional[str] = None
    ISO3: Optional[str] = None
    Specie: Optional[Union[str, "SpecieEnum"]] = None
    Breed: Optional[str] = None
    Description_Of_Specific_Uses: Optional[str] = None
    Lang: Optional[str] = None
    Description: Optional[str] = None
    Transboundary_name: Optional[Union[str, List[str]]] = empty_list()
    Other_name: Optional[str] = None
    Uses: Optional[str] = None
    Additional_information: Optional[str] = None
    Additional_information_comments: Optional[str] = None
    Efabis_cultural_role_comment: Optional[str] = None
    Efabis_cultural_value: Optional[str] = None
    Adaptability_to_specific_environment: Optional[str] = None
    Specific_resistance_or_tolerance: Optional[str] = None
    Specific_reproductive_characteristic: Optional[str] = None
    Special_characteristic_of_product: Optional[str] = None
    Other_special_qualities: Optional[str] = None
    Reference_for_special_qualities: Optional[str] = None
    Efabis_genetic_features: Optional[str] = None
    Efabis_environmental_role: Optional[str] = None
    Efabis_adaptability_to_marginal_land: Optional[str] = None
    Body_conformation: Optional[str] = None
    Coat_description: Optional[str] = None
    Coat_quality: Optional[str] = None
    Comb_type: Optional[Union[str, "CombTypeEnum"]] = None
    Skin_colour: Optional[Union[str, "SkinColourEnum"]] = None
    Shank_and_foot_colour: Optional[Union[str, "ShankAndFootColourEnum"]] = None
    Plumage_colour: Optional[Union[str, "PlumageColourEnum"]] = None
    Pattern_within_feather: Optional[Union[str, "PatternWithinFeatherEnum"]] = None
    Avian_classification: Optional[Union[str, "AvianClassificationEnum"]] = None
    Color_comments: Optional[str] = None
    Efabis_main_colour: Optional[str] = None
    Efabis_skin_colour: Optional[str] = None
    Number_of_horns_males: Optional[Union[str, "NumberOfHornsMalesEnum"]] = None
    Number_of_horns_females: Optional[Union[str, "NumberOfHornsFemalesEnum"]] = None
    Horn_shape_size_and_comments: Optional[str] = None
    Wither_height_males: Optional[float] = None
    Wither_height_females: Optional[float] = None
    Weight_males: Optional[float] = None
    Weight_females: Optional[float] = None
    Other_specific_visible_traits: Optional[str] = None
    Breed_classification: Optional[Union[str, "BreedClassificationEnum"]] = None
    Herdbook: Optional[Union[str, "HerdbookEnum"]] = None
    Herdbook_established: Optional[str] = None
    Domestication_status: Optional[Union[str, "DomesticationStatusEnum"]] = None
    Taxonomic_classification: Optional[Union[str, "TaxonomicClassificationEnum"]] = None
    Description_of_origin: Optional[str] = None
    Year_of_origin: Optional[str] = None
    Import: Optional[str] = None
    Location_within_country: Optional[str] = None
    Eggs_per_year_AVG: Optional[Union[str, XSDDateTime]] = None
    Eggs_per_year_MIN: Optional[int] = None
    Eggs_per_year_MAX: Optional[int] = None
    Egg_weight: Optional[float] = None
    Wool_or_hair: Optional[Union[str, "WoolOrHairEnum"]] = None
    Wool_type: Optional[Union[str, "WoolTypeEnum"]] = None
    Fleece_weight_AVG: Optional[float] = None
    Fleece_weight_MIN: Optional[float] = None
    Fleece_weight_MAX: Optional[float] = None
    Fibre_diam: Optional[float] = None
    Management_system: Optional[str] = None
    Feeding_of_adults: Optional[str] = None
    Mobility: Optional[str] = None
    Milk_per_year_AVG: Optional[float] = None
    Milk_per_year_MIN: Optional[int] = None
    Milk_per_year_MAX: Optional[int] = None
    Lactation_length_AVG: Optional[float] = None
    Lactation_length_MIN: Optional[int] = None
    Lactation_length_MAX: Optional[int] = None
    Milk_yield_per_lactation_(kg)_AVG: Optional[float] = None
    Milk_yield_per_lactation_(kg)_MIN: Optional[float] = None
    Milk_yield_per_lactation_(kg)_MAX: Optional[float] = None
    Milk_fat_AVG: Optional[float] = None
    Milk_fat_MIN: Optional[float] = None
    Milk_fat_MAX: Optional[float] = None
    Milk_per_day: Optional[float] = None
    Number_of_lactations: Optional[float] = None
    Efabis_milk_protein_AVG: Optional[float] = None
    Efabis_milk_protein_MIN: Optional[float] = None
    Efabis_milk_protein_MAX: Optional[float] = None
    Birth_weight_males: Optional[float] = None
    Birth_weight_females: Optional[float] = None
    Age_maturity_males: Optional[float] = None
    Age_maturity_females: Optional[float] = None
    Age_breeding_males: Optional[float] = None
    Age_breeding_females: Optional[float] = None
    Age_first_parturition_AVG: Optional[float] = None
    Age_first_parturition_MIN: Optional[float] = None
    Age_first_parturition_MAX: Optional[float] = None
    Parturition_interval_AVG: Optional[float] = None
    Parturition_interval_MIN: Optional[int] = None
    Parturition_interval_MAX: Optional[int] = None
    Length_productive_life: Optional[float] = None
    Daily_gain: Optional[float] = None
    Carcass_weight: Optional[float] = None
    Dressing_percentage: Optional[float] = None
    Performance_data_reference: Optional[str] = None
    Managment_conditions_performance_measured: Optional[str] = None
    Comments_managment_conditions: Optional[str] = None
    Additional_performance_parameters: Optional[str] = None
    Litter_size_AVG: Optional[float] = None
    Litter_size_MIN: Optional[float] = None
    Litter_size_MAX: Optional[float] = None
    Geographical_classification: Optional[Union[str, "GeographicalClassificationEnum"]] = None
    Local_cryo_conservation_status: Optional[Union[str, "LocalCryoConservationStatusEnum"]] = None
    Local_Risk: Optional[Union[str, "LocalRiskEnum"]] = None
    Detailed_local_risk_status: Optional[Union[str, "DetailedLocalRiskStatusEnum"]] = None
    Regional_Transboundary_Risk_(detailed): Optional[Union[str, "RegionalTransboundaryRisk(detailed)Enum"]] = None
    International_Transboundary_Risk_(detailed): Optional[Union[str, "InternationalTransboundaryRisk(detailed)Enum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Country is not None and not isinstance(self.Country, str):
            self.Country = str(self.Country)

        if self.ISO3 is not None and not isinstance(self.ISO3, str):
            self.ISO3 = str(self.ISO3)

        if self.Specie is not None and not isinstance(self.Specie, SpecieEnum):
            self.Specie = SpecieEnum(self.Specie)

        if self.Breed is not None and not isinstance(self.Breed, str):
            self.Breed = str(self.Breed)

        if self.Description_Of_Specific_Uses is not None and not isinstance(self.Description_Of_Specific_Uses, str):
            self.Description_Of_Specific_Uses = str(self.Description_Of_Specific_Uses)

        if self.Lang is not None and not isinstance(self.Lang, str):
            self.Lang = str(self.Lang)

        if self.Description is not None and not isinstance(self.Description, str):
            self.Description = str(self.Description)

        if not isinstance(self.Transboundary_name, list):
            self.Transboundary_name = [self.Transboundary_name] if self.Transboundary_name is not None else []
        self.Transboundary_name = [v if isinstance(v, str) else str(v) for v in self.Transboundary_name]

        if self.Other_name is not None and not isinstance(self.Other_name, str):
            self.Other_name = str(self.Other_name)

        if self.Uses is not None and not isinstance(self.Uses, str):
            self.Uses = str(self.Uses)

        if self.Additional_information is not None and not isinstance(self.Additional_information, str):
            self.Additional_information = str(self.Additional_information)

        if self.Additional_information_comments is not None and not isinstance(self.Additional_information_comments, str):
            self.Additional_information_comments = str(self.Additional_information_comments)

        if self.Efabis_cultural_role_comment is not None and not isinstance(self.Efabis_cultural_role_comment, str):
            self.Efabis_cultural_role_comment = str(self.Efabis_cultural_role_comment)

        if self.Efabis_cultural_value is not None and not isinstance(self.Efabis_cultural_value, str):
            self.Efabis_cultural_value = str(self.Efabis_cultural_value)

        if self.Adaptability_to_specific_environment is not None and not isinstance(self.Adaptability_to_specific_environment, str):
            self.Adaptability_to_specific_environment = str(self.Adaptability_to_specific_environment)

        if self.Specific_resistance_or_tolerance is not None and not isinstance(self.Specific_resistance_or_tolerance, str):
            self.Specific_resistance_or_tolerance = str(self.Specific_resistance_or_tolerance)

        if self.Specific_reproductive_characteristic is not None and not isinstance(self.Specific_reproductive_characteristic, str):
            self.Specific_reproductive_characteristic = str(self.Specific_reproductive_characteristic)

        if self.Special_characteristic_of_product is not None and not isinstance(self.Special_characteristic_of_product, str):
            self.Special_characteristic_of_product = str(self.Special_characteristic_of_product)

        if self.Other_special_qualities is not None and not isinstance(self.Other_special_qualities, str):
            self.Other_special_qualities = str(self.Other_special_qualities)

        if self.Reference_for_special_qualities is not None and not isinstance(self.Reference_for_special_qualities, str):
            self.Reference_for_special_qualities = str(self.Reference_for_special_qualities)

        if self.Efabis_genetic_features is not None and not isinstance(self.Efabis_genetic_features, str):
            self.Efabis_genetic_features = str(self.Efabis_genetic_features)

        if self.Efabis_environmental_role is not None and not isinstance(self.Efabis_environmental_role, str):
            self.Efabis_environmental_role = str(self.Efabis_environmental_role)

        if self.Efabis_adaptability_to_marginal_land is not None and not isinstance(self.Efabis_adaptability_to_marginal_land, str):
            self.Efabis_adaptability_to_marginal_land = str(self.Efabis_adaptability_to_marginal_land)

        if self.Body_conformation is not None and not isinstance(self.Body_conformation, str):
            self.Body_conformation = str(self.Body_conformation)

        if self.Coat_description is not None and not isinstance(self.Coat_description, str):
            self.Coat_description = str(self.Coat_description)

        if self.Coat_quality is not None and not isinstance(self.Coat_quality, str):
            self.Coat_quality = str(self.Coat_quality)

        if self.Comb_type is not None and not isinstance(self.Comb_type, CombTypeEnum):
            self.Comb_type = CombTypeEnum(self.Comb_type)

        if self.Skin_colour is not None and not isinstance(self.Skin_colour, SkinColourEnum):
            self.Skin_colour = SkinColourEnum(self.Skin_colour)

        if self.Shank_and_foot_colour is not None and not isinstance(self.Shank_and_foot_colour, ShankAndFootColourEnum):
            self.Shank_and_foot_colour = ShankAndFootColourEnum(self.Shank_and_foot_colour)

        if self.Plumage_colour is not None and not isinstance(self.Plumage_colour, PlumageColourEnum):
            self.Plumage_colour = PlumageColourEnum(self.Plumage_colour)

        if self.Pattern_within_feather is not None and not isinstance(self.Pattern_within_feather, PatternWithinFeatherEnum):
            self.Pattern_within_feather = PatternWithinFeatherEnum(self.Pattern_within_feather)

        if self.Avian_classification is not None and not isinstance(self.Avian_classification, AvianClassificationEnum):
            self.Avian_classification = AvianClassificationEnum(self.Avian_classification)

        if self.Color_comments is not None and not isinstance(self.Color_comments, str):
            self.Color_comments = str(self.Color_comments)

        if self.Efabis_main_colour is not None and not isinstance(self.Efabis_main_colour, str):
            self.Efabis_main_colour = str(self.Efabis_main_colour)

        if self.Efabis_skin_colour is not None and not isinstance(self.Efabis_skin_colour, str):
            self.Efabis_skin_colour = str(self.Efabis_skin_colour)

        if self.Number_of_horns_males is not None and not isinstance(self.Number_of_horns_males, NumberOfHornsMalesEnum):
            self.Number_of_horns_males = NumberOfHornsMalesEnum(self.Number_of_horns_males)

        if self.Number_of_horns_females is not None and not isinstance(self.Number_of_horns_females, NumberOfHornsFemalesEnum):
            self.Number_of_horns_females = NumberOfHornsFemalesEnum(self.Number_of_horns_females)

        if self.Horn_shape_size_and_comments is not None and not isinstance(self.Horn_shape_size_and_comments, str):
            self.Horn_shape_size_and_comments = str(self.Horn_shape_size_and_comments)

        if self.Wither_height_males is not None and not isinstance(self.Wither_height_males, float):
            self.Wither_height_males = float(self.Wither_height_males)

        if self.Wither_height_females is not None and not isinstance(self.Wither_height_females, float):
            self.Wither_height_females = float(self.Wither_height_females)

        if self.Weight_males is not None and not isinstance(self.Weight_males, float):
            self.Weight_males = float(self.Weight_males)

        if self.Weight_females is not None and not isinstance(self.Weight_females, float):
            self.Weight_females = float(self.Weight_females)

        if self.Other_specific_visible_traits is not None and not isinstance(self.Other_specific_visible_traits, str):
            self.Other_specific_visible_traits = str(self.Other_specific_visible_traits)

        if self.Breed_classification is not None and not isinstance(self.Breed_classification, BreedClassificationEnum):
            self.Breed_classification = BreedClassificationEnum(self.Breed_classification)

        if self.Herdbook is not None and not isinstance(self.Herdbook, HerdbookEnum):
            self.Herdbook = HerdbookEnum(self.Herdbook)

        if self.Herdbook_established is not None and not isinstance(self.Herdbook_established, str):
            self.Herdbook_established = str(self.Herdbook_established)

        if self.Domestication_status is not None and not isinstance(self.Domestication_status, DomesticationStatusEnum):
            self.Domestication_status = DomesticationStatusEnum(self.Domestication_status)

        if self.Taxonomic_classification is not None and not isinstance(self.Taxonomic_classification, TaxonomicClassificationEnum):
            self.Taxonomic_classification = TaxonomicClassificationEnum(self.Taxonomic_classification)

        if self.Description_of_origin is not None and not isinstance(self.Description_of_origin, str):
            self.Description_of_origin = str(self.Description_of_origin)

        if self.Year_of_origin is not None and not isinstance(self.Year_of_origin, str):
            self.Year_of_origin = str(self.Year_of_origin)

        if self.Import is not None and not isinstance(self.Import, str):
            self.Import = str(self.Import)

        if self.Location_within_country is not None and not isinstance(self.Location_within_country, str):
            self.Location_within_country = str(self.Location_within_country)

        if self.Eggs_per_year_AVG is not None and not isinstance(self.Eggs_per_year_AVG, XSDDateTime):
            self.Eggs_per_year_AVG = XSDDateTime(self.Eggs_per_year_AVG)

        if self.Eggs_per_year_MIN is not None and not isinstance(self.Eggs_per_year_MIN, int):
            self.Eggs_per_year_MIN = int(self.Eggs_per_year_MIN)

        if self.Eggs_per_year_MAX is not None and not isinstance(self.Eggs_per_year_MAX, int):
            self.Eggs_per_year_MAX = int(self.Eggs_per_year_MAX)

        if self.Egg_weight is not None and not isinstance(self.Egg_weight, float):
            self.Egg_weight = float(self.Egg_weight)

        if self.Wool_or_hair is not None and not isinstance(self.Wool_or_hair, WoolOrHairEnum):
            self.Wool_or_hair = WoolOrHairEnum(self.Wool_or_hair)

        if self.Wool_type is not None and not isinstance(self.Wool_type, WoolTypeEnum):
            self.Wool_type = WoolTypeEnum(self.Wool_type)

        if self.Fleece_weight_AVG is not None and not isinstance(self.Fleece_weight_AVG, float):
            self.Fleece_weight_AVG = float(self.Fleece_weight_AVG)

        if self.Fleece_weight_MIN is not None and not isinstance(self.Fleece_weight_MIN, float):
            self.Fleece_weight_MIN = float(self.Fleece_weight_MIN)

        if self.Fleece_weight_MAX is not None and not isinstance(self.Fleece_weight_MAX, float):
            self.Fleece_weight_MAX = float(self.Fleece_weight_MAX)

        if self.Fibre_diam is not None and not isinstance(self.Fibre_diam, float):
            self.Fibre_diam = float(self.Fibre_diam)

        if self.Management_system is not None and not isinstance(self.Management_system, str):
            self.Management_system = str(self.Management_system)

        if self.Feeding_of_adults is not None and not isinstance(self.Feeding_of_adults, str):
            self.Feeding_of_adults = str(self.Feeding_of_adults)

        if self.Mobility is not None and not isinstance(self.Mobility, str):
            self.Mobility = str(self.Mobility)

        if self.Milk_per_year_AVG is not None and not isinstance(self.Milk_per_year_AVG, float):
            self.Milk_per_year_AVG = float(self.Milk_per_year_AVG)

        if self.Milk_per_year_MIN is not None and not isinstance(self.Milk_per_year_MIN, int):
            self.Milk_per_year_MIN = int(self.Milk_per_year_MIN)

        if self.Milk_per_year_MAX is not None and not isinstance(self.Milk_per_year_MAX, int):
            self.Milk_per_year_MAX = int(self.Milk_per_year_MAX)

        if self.Lactation_length_AVG is not None and not isinstance(self.Lactation_length_AVG, float):
            self.Lactation_length_AVG = float(self.Lactation_length_AVG)

        if self.Lactation_length_MIN is not None and not isinstance(self.Lactation_length_MIN, int):
            self.Lactation_length_MIN = int(self.Lactation_length_MIN)

        if self.Lactation_length_MAX is not None and not isinstance(self.Lactation_length_MAX, int):
            self.Lactation_length_MAX = int(self.Lactation_length_MAX)

        if self.Milk_yield_per_lactation_(kg)_AVG is not None and not isinstance(self.Milk_yield_per_lactation_(kg)_AVG, float):
            self.Milk_yield_per_lactation_(kg)_AVG = float(self.Milk_yield_per_lactation_(kg)_AVG)

        if self.Milk_yield_per_lactation_(kg)_MIN is not None and not isinstance(self.Milk_yield_per_lactation_(kg)_MIN, float):
            self.Milk_yield_per_lactation_(kg)_MIN = float(self.Milk_yield_per_lactation_(kg)_MIN)

        if self.Milk_yield_per_lactation_(kg)_MAX is not None and not isinstance(self.Milk_yield_per_lactation_(kg)_MAX, float):
            self.Milk_yield_per_lactation_(kg)_MAX = float(self.Milk_yield_per_lactation_(kg)_MAX)

        if self.Milk_fat_AVG is not None and not isinstance(self.Milk_fat_AVG, float):
            self.Milk_fat_AVG = float(self.Milk_fat_AVG)

        if self.Milk_fat_MIN is not None and not isinstance(self.Milk_fat_MIN, float):
            self.Milk_fat_MIN = float(self.Milk_fat_MIN)

        if self.Milk_fat_MAX is not None and not isinstance(self.Milk_fat_MAX, float):
            self.Milk_fat_MAX = float(self.Milk_fat_MAX)

        if self.Milk_per_day is not None and not isinstance(self.Milk_per_day, float):
            self.Milk_per_day = float(self.Milk_per_day)

        if self.Number_of_lactations is not None and not isinstance(self.Number_of_lactations, float):
            self.Number_of_lactations = float(self.Number_of_lactations)

        if self.Efabis_milk_protein_AVG is not None and not isinstance(self.Efabis_milk_protein_AVG, float):
            self.Efabis_milk_protein_AVG = float(self.Efabis_milk_protein_AVG)

        if self.Efabis_milk_protein_MIN is not None and not isinstance(self.Efabis_milk_protein_MIN, float):
            self.Efabis_milk_protein_MIN = float(self.Efabis_milk_protein_MIN)

        if self.Efabis_milk_protein_MAX is not None and not isinstance(self.Efabis_milk_protein_MAX, float):
            self.Efabis_milk_protein_MAX = float(self.Efabis_milk_protein_MAX)

        if self.Birth_weight_males is not None and not isinstance(self.Birth_weight_males, float):
            self.Birth_weight_males = float(self.Birth_weight_males)

        if self.Birth_weight_females is not None and not isinstance(self.Birth_weight_females, float):
            self.Birth_weight_females = float(self.Birth_weight_females)

        if self.Age_maturity_males is not None and not isinstance(self.Age_maturity_males, float):
            self.Age_maturity_males = float(self.Age_maturity_males)

        if self.Age_maturity_females is not None and not isinstance(self.Age_maturity_females, float):
            self.Age_maturity_females = float(self.Age_maturity_females)

        if self.Age_breeding_males is not None and not isinstance(self.Age_breeding_males, float):
            self.Age_breeding_males = float(self.Age_breeding_males)

        if self.Age_breeding_females is not None and not isinstance(self.Age_breeding_females, float):
            self.Age_breeding_females = float(self.Age_breeding_females)

        if self.Age_first_parturition_AVG is not None and not isinstance(self.Age_first_parturition_AVG, float):
            self.Age_first_parturition_AVG = float(self.Age_first_parturition_AVG)

        if self.Age_first_parturition_MIN is not None and not isinstance(self.Age_first_parturition_MIN, float):
            self.Age_first_parturition_MIN = float(self.Age_first_parturition_MIN)

        if self.Age_first_parturition_MAX is not None and not isinstance(self.Age_first_parturition_MAX, float):
            self.Age_first_parturition_MAX = float(self.Age_first_parturition_MAX)

        if self.Parturition_interval_AVG is not None and not isinstance(self.Parturition_interval_AVG, float):
            self.Parturition_interval_AVG = float(self.Parturition_interval_AVG)

        if self.Parturition_interval_MIN is not None and not isinstance(self.Parturition_interval_MIN, int):
            self.Parturition_interval_MIN = int(self.Parturition_interval_MIN)

        if self.Parturition_interval_MAX is not None and not isinstance(self.Parturition_interval_MAX, int):
            self.Parturition_interval_MAX = int(self.Parturition_interval_MAX)

        if self.Length_productive_life is not None and not isinstance(self.Length_productive_life, float):
            self.Length_productive_life = float(self.Length_productive_life)

        if self.Daily_gain is not None and not isinstance(self.Daily_gain, float):
            self.Daily_gain = float(self.Daily_gain)

        if self.Carcass_weight is not None and not isinstance(self.Carcass_weight, float):
            self.Carcass_weight = float(self.Carcass_weight)

        if self.Dressing_percentage is not None and not isinstance(self.Dressing_percentage, float):
            self.Dressing_percentage = float(self.Dressing_percentage)

        if self.Performance_data_reference is not None and not isinstance(self.Performance_data_reference, str):
            self.Performance_data_reference = str(self.Performance_data_reference)

        if self.Managment_conditions_performance_measured is not None and not isinstance(self.Managment_conditions_performance_measured, str):
            self.Managment_conditions_performance_measured = str(self.Managment_conditions_performance_measured)

        if self.Comments_managment_conditions is not None and not isinstance(self.Comments_managment_conditions, str):
            self.Comments_managment_conditions = str(self.Comments_managment_conditions)

        if self.Additional_performance_parameters is not None and not isinstance(self.Additional_performance_parameters, str):
            self.Additional_performance_parameters = str(self.Additional_performance_parameters)

        if self.Litter_size_AVG is not None and not isinstance(self.Litter_size_AVG, float):
            self.Litter_size_AVG = float(self.Litter_size_AVG)

        if self.Litter_size_MIN is not None and not isinstance(self.Litter_size_MIN, float):
            self.Litter_size_MIN = float(self.Litter_size_MIN)

        if self.Litter_size_MAX is not None and not isinstance(self.Litter_size_MAX, float):
            self.Litter_size_MAX = float(self.Litter_size_MAX)

        if self.Geographical_classification is not None and not isinstance(self.Geographical_classification, GeographicalClassificationEnum):
            self.Geographical_classification = GeographicalClassificationEnum(self.Geographical_classification)

        if self.Local_cryo_conservation_status is not None and not isinstance(self.Local_cryo_conservation_status, LocalCryoConservationStatusEnum):
            self.Local_cryo_conservation_status = LocalCryoConservationStatusEnum(self.Local_cryo_conservation_status)

        if self.Local_Risk is not None and not isinstance(self.Local_Risk, LocalRiskEnum):
            self.Local_Risk = LocalRiskEnum(self.Local_Risk)

        if self.Detailed_local_risk_status is not None and not isinstance(self.Detailed_local_risk_status, DetailedLocalRiskStatusEnum):
            self.Detailed_local_risk_status = DetailedLocalRiskStatusEnum(self.Detailed_local_risk_status)

        if self.Regional_Transboundary_Risk_(detailed) is not None and not isinstance(self.Regional_Transboundary_Risk_(detailed), RegionalTransboundaryRisk(detailed)Enum):
            self.Regional_Transboundary_Risk_(detailed) = RegionalTransboundaryRisk(detailed)Enum(self.Regional_Transboundary_Risk_(detailed))

        if self.International_Transboundary_Risk_(detailed) is not None and not isinstance(self.International_Transboundary_Risk_(detailed), InternationalTransboundaryRisk(detailed)Enum):
            self.International_Transboundary_Risk_(detailed) = InternationalTransboundaryRisk(detailed)Enum(self.International_Transboundary_Risk_(detailed))

        super().__post_init__(**kwargs)


@dataclass
class Indicator(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = EXAMPLE.Indicator
    class_class_curie: ClassVar[str] = "example:Indicator"
    class_name: ClassVar[str] = "Indicator"
    class_model_uri: ClassVar[URIRef] = EXAMPLE.Indicator

    Indicator_Reference_Number: Optional[Union[str, XSDDateTime]] = None
    Series_Name: Optional[int] = None
    Series_Description: Optional[str] = None
    Geo_Area_Code: Optional[int] = None
    Geo_Area_Name: Optional[str] = None
    Year: Optional[int] = None
    Reference_Area_Type_(Countries): Optional[str] = None
    Indicator_value: Optional[str] = None
    Unit_of_Measurement: Optional[Union[str, "UnitOfMeasurementEnum"]] = None
    Nature: Optional[Union[str, "NatureEnum"]] = None
    Reporting_Type: Optional[Union[str, "ReportingTypeEnum"]] = None
    Number_of_local_breeds_(not_extinct): Optional[int] = None
    Number_of_local_breeds_with_unknown_status: Optional[int] = None
    Number_of_local_breeds_at_risk: Optional[int] = None
    Number_of_local_breeds_not_at_risk: Optional[int] = None
    Source_Detail: Optional[Union[str, DAD-IS7.9.2021HttpIdentifier]] = None
    Foot_Notes: Optional[str] = None
    SDG_Region_Code: Optional[int] = None
    SDG_Region_Name: Optional[str] = None
    M49_Level_1_Code: Optional[int] = None
    M49_Level_1_Region: Optional[Union[str, "M49Level-1RegionEnum"]] = None
    M49_Level_2_Code: Optional[int] = None
    M49_Level_2_Name: Optional[str] = None
    M49_Intermediate_Code: Optional[int] = None
    M49_Intermediate_Name: Optional[Union[str, "M49IntermediateNameEnum"]] = None
    MDG_Code: Optional[int] = None
    MDG_Regions: Optional[str] = None
    LDCs_Code: Optional[int] = None
    LDCs_Name: Optional[str] = None
    LLDCs_Code: Optional[int] = None
    LLDCs_Name: Optional[str] = None
    Number_of_countries_or_territories_in_the_region: Optional[int] = None
    Number_of_countries_or_territories_with_valid_data: Optional[int] = None
    Percentage_of_countries_or_territories_with_valid_data: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.Indicator_Reference_Number is not None and not isinstance(self.Indicator_Reference_Number, XSDDateTime):
            self.Indicator_Reference_Number = XSDDateTime(self.Indicator_Reference_Number)

        if self.Series_Name is not None and not isinstance(self.Series_Name, int):
            self.Series_Name = int(self.Series_Name)

        if self.Series_Description is not None and not isinstance(self.Series_Description, str):
            self.Series_Description = str(self.Series_Description)

        if self.Geo_Area_Code is not None and not isinstance(self.Geo_Area_Code, int):
            self.Geo_Area_Code = int(self.Geo_Area_Code)

        if self.Geo_Area_Name is not None and not isinstance(self.Geo_Area_Name, str):
            self.Geo_Area_Name = str(self.Geo_Area_Name)

        if self.Year is not None and not isinstance(self.Year, int):
            self.Year = int(self.Year)

        if self.Reference_Area_Type_(Countries) is not None and not isinstance(self.Reference_Area_Type_(Countries), str):
            self.Reference_Area_Type_(Countries) = str(self.Reference_Area_Type_(Countries))

        if self.Indicator_value is not None and not isinstance(self.Indicator_value, str):
            self.Indicator_value = str(self.Indicator_value)

        if self.Unit_of_Measurement is not None and not isinstance(self.Unit_of_Measurement, UnitOfMeasurementEnum):
            self.Unit_of_Measurement = UnitOfMeasurementEnum(self.Unit_of_Measurement)

        if self.Nature is not None and not isinstance(self.Nature, NatureEnum):
            self.Nature = NatureEnum(self.Nature)

        if self.Reporting_Type is not None and not isinstance(self.Reporting_Type, ReportingTypeEnum):
            self.Reporting_Type = ReportingTypeEnum(self.Reporting_Type)

        if self.Number_of_local_breeds_(not_extinct) is not None and not isinstance(self.Number_of_local_breeds_(not_extinct), int):
            self.Number_of_local_breeds_(not_extinct) = int(self.Number_of_local_breeds_(not_extinct))

        if self.Number_of_local_breeds_with_unknown_status is not None and not isinstance(self.Number_of_local_breeds_with_unknown_status, int):
            self.Number_of_local_breeds_with_unknown_status = int(self.Number_of_local_breeds_with_unknown_status)

        if self.Number_of_local_breeds_at_risk is not None and not isinstance(self.Number_of_local_breeds_at_risk, int):
            self.Number_of_local_breeds_at_risk = int(self.Number_of_local_breeds_at_risk)

        if self.Number_of_local_breeds_not_at_risk is not None and not isinstance(self.Number_of_local_breeds_not_at_risk, int):
            self.Number_of_local_breeds_not_at_risk = int(self.Number_of_local_breeds_not_at_risk)

        if self.Source_Detail is not None and not isinstance(self.Source_Detail, DAD-IS7.9.2021HttpIdentifier):
            self.Source_Detail = DAD-IS7.9.2021HttpIdentifier(self.Source_Detail)

        if self.Foot_Notes is not None and not isinstance(self.Foot_Notes, str):
            self.Foot_Notes = str(self.Foot_Notes)

        if self.SDG_Region_Code is not None and not isinstance(self.SDG_Region_Code, int):
            self.SDG_Region_Code = int(self.SDG_Region_Code)

        if self.SDG_Region_Name is not None and not isinstance(self.SDG_Region_Name, str):
            self.SDG_Region_Name = str(self.SDG_Region_Name)

        if self.M49_Level_1_Code is not None and not isinstance(self.M49_Level_1_Code, int):
            self.M49_Level_1_Code = int(self.M49_Level_1_Code)

        if self.M49_Level_1_Region is not None and not isinstance(self.M49_Level_1_Region, M49Level-1RegionEnum):
            self.M49_Level_1_Region = M49Level-1RegionEnum(self.M49_Level_1_Region)

        if self.M49_Level_2_Code is not None and not isinstance(self.M49_Level_2_Code, int):
            self.M49_Level_2_Code = int(self.M49_Level_2_Code)

        if self.M49_Level_2_Name is not None and not isinstance(self.M49_Level_2_Name, str):
            self.M49_Level_2_Name = str(self.M49_Level_2_Name)

        if self.M49_Intermediate_Code is not None and not isinstance(self.M49_Intermediate_Code, int):
            self.M49_Intermediate_Code = int(self.M49_Intermediate_Code)

        if self.M49_Intermediate_Name is not None and not isinstance(self.M49_Intermediate_Name, M49IntermediateNameEnum):
            self.M49_Intermediate_Name = M49IntermediateNameEnum(self.M49_Intermediate_Name)

        if self.MDG_Code is not None and not isinstance(self.MDG_Code, int):
            self.MDG_Code = int(self.MDG_Code)

        if self.MDG_Regions is not None and not isinstance(self.MDG_Regions, str):
            self.MDG_Regions = str(self.MDG_Regions)

        if self.LDCs_Code is not None and not isinstance(self.LDCs_Code, int):
            self.LDCs_Code = int(self.LDCs_Code)

        if self.LDCs_Name is not None and not isinstance(self.LDCs_Name, str):
            self.LDCs_Name = str(self.LDCs_Name)

        if self.LLDCs_Code is not None and not isinstance(self.LLDCs_Code, int):
            self.LLDCs_Code = int(self.LLDCs_Code)

        if self.LLDCs_Name is not None and not isinstance(self.LLDCs_Name, str):
            self.LLDCs_Name = str(self.LLDCs_Name)

        if self.Number_of_countries_or_territories_in_the_region is not None and not isinstance(self.Number_of_countries_or_territories_in_the_region, int):
            self.Number_of_countries_or_territories_in_the_region = int(self.Number_of_countries_or_territories_in_the_region)

        if self.Number_of_countries_or_territories_with_valid_data is not None and not isinstance(self.Number_of_countries_or_territories_with_valid_data, int):
            self.Number_of_countries_or_territories_with_valid_data = int(self.Number_of_countries_or_territories_with_valid_data)

        if self.Percentage_of_countries_or_territories_with_valid_data is not None and not isinstance(self.Percentage_of_countries_or_territories_with_valid_data, float):
            self.Percentage_of_countries_or_territories_with_valid_data = float(self.Percentage_of_countries_or_territories_with_valid_data)

        super().__post_init__(**kwargs)


# Enumerations
class SpecieEnum(EnumDefinitionImpl):

    Horse = PermissibleValue(text="Horse",
                                 description="Horse")
    Deer = PermissibleValue(text="Deer",
                               description="Deer")
    Rabbit = PermissibleValue(text="Rabbit",
                                   description="Rabbit")
    Llama = PermissibleValue(text="Llama",
                                 description="Llama")
    Peacock = PermissibleValue(text="Peacock",
                                     description="Peacock")
    Pigeon = PermissibleValue(text="Pigeon",
                                   description="Pigeon")
    Cattle = PermissibleValue(text="Cattle",
                                   description="Cattle")
    Goat = PermissibleValue(text="Goat",
                               description="Goat")
    Partridge = PermissibleValue(text="Partridge",
                                         description="Partridge")
    Quail = PermissibleValue(text="Quail",
                                 description="Quail")
    Ass = PermissibleValue(text="Ass",
                             description="Ass")
    Pheasant = PermissibleValue(text="Pheasant",
                                       description="Pheasant")
    Alpaca = PermissibleValue(text="Alpaca",
                                   description="Alpaca")
    Ostrich = PermissibleValue(text="Ostrich",
                                     description="Ostrich")
    Buffalo = PermissibleValue(text="Buffalo",
                                     description="Buffalo")
    Guanaco = PermissibleValue(text="Guanaco",
                                     description="Guanaco")
    Chicken = PermissibleValue(text="Chicken",
                                     description="Chicken")
    Nandu = PermissibleValue(text="Nandu",
                                 description="Nandu")
    Dromedary = PermissibleValue(text="Dromedary",
                                         description="Dromedary")
    Sheep = PermissibleValue(text="Sheep",
                                 description="Sheep")
    Turkey = PermissibleValue(text="Turkey",
                                   description="Turkey")
    Swallow = PermissibleValue(text="Swallow",
                                     description="Swallow")
    Cassowary = PermissibleValue(text="Cassowary",
                                         description="Cassowary")
    Emu = PermissibleValue(text="Emu",
                             description="Emu")
    Dog = PermissibleValue(text="Dog",
                             description="Dog")
    Vicuña = PermissibleValue(text="Vicuña",
                                   description="Vicuña")
    Pig = PermissibleValue(text="Pig",
                             description="Pig")

    _defn = EnumDefinition(
        name="SpecieEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Goose (domestic)",
                PermissibleValue(text="Goose (domestic)",
                                 description="Goose (domestic)") )
        setattr(cls, "Dromedary Bactrian Camel",
                PermissibleValue(text="Dromedary Bactrian Camel",
                                 description="Dromedary Bactrian Camel") )
        setattr(cls, "Guinea pig",
                PermissibleValue(text="Guinea pig",
                                 description="Guinea pig") )
        setattr(cls, "American Bison",
                PermissibleValue(text="American Bison",
                                 description="American Bison") )
        setattr(cls, "Guinea fowl",
                PermissibleValue(text="Guinea fowl",
                                 description="Guinea fowl") )
        setattr(cls, "Duck(domestic) Muscovy duck",
                PermissibleValue(text="Duck(domestic) Muscovy duck",
                                 description="Duck(domestic) Muscovy duck") )
        setattr(cls, "Yak (domestic)",
                PermissibleValue(text="Yak (domestic)",
                                 description="Yak (domestic)") )
        setattr(cls, "Bactrian camel",
                PermissibleValue(text="Bactrian camel",
                                 description="Bactrian camel") )
        setattr(cls, "Muscovy duck",
                PermissibleValue(text="Muscovy duck",
                                 description="Muscovy duck") )
        setattr(cls, "Duck (domestic)",
                PermissibleValue(text="Duck (domestic)",
                                 description="Duck (domestic)") )

class CombTypeEnum(EnumDefinitionImpl):

    walnut = PermissibleValue(text="walnut",
                                   description="walnut")
    Single = PermissibleValue(text="Single",
                                   description="Single")
    pea = PermissibleValue(text="pea",
                             description="pea")
    rose = PermissibleValue(text="rose",
                               description="rose")
    single = PermissibleValue(text="single",
                                   description="single")

    _defn = EnumDefinition(
        name="CombTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Duplex or V-shaped",
                PermissibleValue(text="Duplex or V-shaped",
                                 description="Duplex or V-shaped") )
        setattr(cls, "duplex or V-shaped",
                PermissibleValue(text="duplex or V-shaped",
                                 description="duplex or V-shaped") )

class SkinColourEnum(EnumDefinitionImpl):

    White = PermissibleValue(text="White",
                                 description="White")
    yellow = PermissibleValue(text="yellow",
                                   description="yellow")
    Yellow = PermissibleValue(text="Yellow",
                                   description="Yellow")
    white = PermissibleValue(text="white",
                                 description="white")

    _defn = EnumDefinition(
        name="SkinColourEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Blue-Black",
                PermissibleValue(text="Blue-Black",
                                 description="Blue-Black") )
        setattr(cls, "blue-black",
                PermissibleValue(text="blue-black",
                                 description="blue-black") )

class ShankAndFootColourEnum(EnumDefinitionImpl):

    green = PermissibleValue(text="green",
                                 description="green")
    reddish = PermissibleValue(text="reddish",
                                     description="reddish")
    various = PermissibleValue(text="various",
                                     description="various")
    Green = PermissibleValue(text="Green",
                                 description="Green")
    Reddish = PermissibleValue(text="Reddish",
                                     description="Reddish")
    grey = PermissibleValue(text="grey",
                               description="grey")
    black = PermissibleValue(text="black",
                                 description="black")
    blue = PermissibleValue(text="blue",
                               description="blue")
    yellow = PermissibleValue(text="yellow",
                                   description="yellow")
    Yellow = PermissibleValue(text="Yellow",
                                   description="Yellow")
    orange = PermissibleValue(text="orange",
                                   description="orange")
    Grey = PermissibleValue(text="Grey",
                               description="Grey")
    Orange = PermissibleValue(text="Orange",
                                   description="Orange")
    white = PermissibleValue(text="white",
                                 description="white")
    Black = PermissibleValue(text="Black",
                                 description="Black")

    _defn = EnumDefinition(
        name="ShankAndFootColourEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "white pinkish",
                PermissibleValue(text="white pinkish",
                                 description="white pinkish") )

class PlumageColourEnum(EnumDefinitionImpl):

    White = PermissibleValue(text="White",
                                 description="White")
    Brown = PermissibleValue(text="Brown",
                                 description="Brown")
    grey = PermissibleValue(text="grey",
                               description="grey")
    yellow = PermissibleValue(text="yellow",
                                   description="yellow")
    brown = PermissibleValue(text="brown",
                                 description="brown")
    red = PermissibleValue(text="red",
                             description="red")
    white = PermissibleValue(text="white",
                                 description="white")

    _defn = EnumDefinition(
        name="PlumageColourEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Grey and White",
                PermissibleValue(text="Grey and White",
                                 description="Grey and White") )
        setattr(cls, "red and brown",
                PermissibleValue(text="red and brown",
                                 description="red and brown") )
        setattr(cls, "silver colombian",
                PermissibleValue(text="silver colombian",
                                 description="silver colombian") )
        setattr(cls, "red and black",
                PermissibleValue(text="red and black",
                                 description="red and black") )
        setattr(cls, "wild type and variants",
                PermissibleValue(text="wild type and variants",
                                 description="wild type and variants") )
        setattr(cls, "white and brown",
                PermissibleValue(text="white and brown",
                                 description="white and brown") )
        setattr(cls, "white and blue",
                PermissibleValue(text="white and blue",
                                 description="white and blue") )
        setattr(cls, "Grey and white",
                PermissibleValue(text="Grey and white",
                                 description="Grey and white") )
        setattr(cls, "Red and Black",
                PermissibleValue(text="Red and Black",
                                 description="Red and Black") )
        setattr(cls, "Various color",
                PermissibleValue(text="Various color",
                                 description="Various color") )
        setattr(cls, "various colours",
                PermissibleValue(text="various colours",
                                 description="various colours") )
        setattr(cls, "self-black",
                PermissibleValue(text="self-black",
                                 description="self-black") )
        setattr(cls, "self-white",
                PermissibleValue(text="self-white",
                                 description="self-white") )
        setattr(cls, "gold-colombian",
                PermissibleValue(text="gold-colombian",
                                 description="gold-colombian") )
        setattr(cls, "grey and white",
                PermissibleValue(text="grey and white",
                                 description="grey and white") )

class PatternWithinFeatherEnum(EnumDefinitionImpl):

    mottled = PermissibleValue(text="mottled",
                                     description="mottled")
    cuckoo = PermissibleValue(text="cuckoo",
                                   description="cuckoo")
    spangled = PermissibleValue(text="spangled",
                                       description="spangled")
    pencilled = PermissibleValue(text="pencilled",
                                         description="pencilled")
    laced = PermissibleValue(text="laced",
                                 description="laced")

    _defn = EnumDefinition(
        name="PatternWithinFeatherEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "barred, autosomal",
                PermissibleValue(text="barred, autosomal",
                                 description="barred, autosomal") )
        setattr(cls, "Barred, sex-linked",
                PermissibleValue(text="Barred, sex-linked",
                                 description="Barred, sex-linked") )
        setattr(cls, "barred, sex-linked",
                PermissibleValue(text="barred, sex-linked",
                                 description="barred, sex-linked") )
        setattr(cls, "Barred, Sex-linked",
                PermissibleValue(text="Barred, Sex-linked",
                                 description="Barred, Sex-linked") )
        setattr(cls, "No special pattern",
                PermissibleValue(text="No special pattern",
                                 description="No special pattern") )
        setattr(cls, "no special pattern",
                PermissibleValue(text="no special pattern",
                                 description="no special pattern") )

class AvianClassificationEnum(EnumDefinitionImpl):

    indigenous = PermissibleValue(text="indigenous",
                                           description="indigenous")
    fancy = PermissibleValue(text="fancy",
                                 description="fancy")
    Indigenous = PermissibleValue(text="Indigenous",
                                           description="Indigenous")
    laboratory = PermissibleValue(text="laboratory",
                                           description="laboratory")
    Industrial = PermissibleValue(text="Industrial",
                                           description="Industrial")
    industrial = PermissibleValue(text="industrial",
                                           description="industrial")
    Fancy = PermissibleValue(text="Fancy",
                                 description="Fancy")
    Laboratory = PermissibleValue(text="Laboratory",
                                           description="Laboratory")

    _defn = EnumDefinition(
        name="AvianClassificationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "middle level",
                PermissibleValue(text="middle level",
                                 description="middle level") )
        setattr(cls, "Middle level",
                PermissibleValue(text="Middle level",
                                 description="Middle level") )

class NumberOfHornsMalesEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NumberOfHornsMalesEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0 / 2 / 4",
                PermissibleValue(text="0 / 2 / 4",
                                 description="0 / 2 / 4") )
        setattr(cls, "4",
                PermissibleValue(text="4",
                                 description="4") )
        setattr(cls, "2/4",
                PermissibleValue(text="2/4",
                                 description="2/4") )
        setattr(cls, "0/2",
                PermissibleValue(text="0/2",
                                 description="0/2") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="2") )
        setattr(cls, "0 / 2",
                PermissibleValue(text="0 / 2",
                                 description="0 / 2") )
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="0") )
        setattr(cls, "0/2/4",
                PermissibleValue(text="0/2/4",
                                 description="0/2/4") )

class NumberOfHornsFemalesEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="NumberOfHornsFemalesEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "0 / 2 / 4",
                PermissibleValue(text="0 / 2 / 4",
                                 description="0 / 2 / 4") )
        setattr(cls, "4",
                PermissibleValue(text="4",
                                 description="4") )
        setattr(cls, "2/4",
                PermissibleValue(text="2/4",
                                 description="2/4") )
        setattr(cls, "0/2",
                PermissibleValue(text="0/2",
                                 description="0/2") )
        setattr(cls, "2",
                PermissibleValue(text="2",
                                 description="2") )
        setattr(cls, "0 / 2",
                PermissibleValue(text="0 / 2",
                                 description="0 / 2") )
        setattr(cls, "0",
                PermissibleValue(text="0",
                                 description="0") )
        setattr(cls, "0/2/4",
                PermissibleValue(text="0/2/4",
                                 description="0/2/4") )

class BreedClassificationEnum(EnumDefinitionImpl):

    Exotic = PermissibleValue(text="Exotic",
                                   description="Exotic")
    Native = PermissibleValue(text="Native",
                                   description="Native")

    _defn = EnumDefinition(
        name="BreedClassificationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Locally adapted",
                PermissibleValue(text="Locally adapted",
                                 description="Locally adapted") )

class HerdbookEnum(EnumDefinitionImpl):

    n = PermissibleValue(text="n",
                         description="n")
    Y = PermissibleValue(text="Y",
                         description="Y")
    y = PermissibleValue(text="y",
                         description="y")

    _defn = EnumDefinition(
        name="HerdbookEnum",
    )

class DomesticationStatusEnum(EnumDefinitionImpl):

    Feral = PermissibleValue(text="Feral",
                                 description="Feral")
    feral = PermissibleValue(text="feral",
                                 description="feral")
    wild = PermissibleValue(text="wild",
                               description="wild")
    domestic = PermissibleValue(text="domestic",
                                       description="domestic")
    Wild = PermissibleValue(text="Wild",
                               description="Wild")
    Domestic = PermissibleValue(text="Domestic",
                                       description="Domestic")

    _defn = EnumDefinition(
        name="DomesticationStatusEnum",
    )

class TaxonomicClassificationEnum(EnumDefinitionImpl):

    Breed = PermissibleValue(text="Breed",
                                 description="Breed")
    breed = PermissibleValue(text="breed",
                                 description="breed")
    variety = PermissibleValue(text="variety",
                                     description="variety")
    Variety = PermissibleValue(text="Variety",
                                     description="Variety")
    Mongrel = PermissibleValue(text="Mongrel",
                                     description="Mongrel")
    strain = PermissibleValue(text="strain",
                                   description="strain")
    Strain = PermissibleValue(text="Strain",
                                   description="Strain")
    Species = PermissibleValue(text="Species",
                                     description="Species")
    line = PermissibleValue(text="line",
                               description="line")
    Line = PermissibleValue(text="Line",
                               description="Line")
    species = PermissibleValue(text="species",
                                     description="species")

    _defn = EnumDefinition(
        name="TaxonomicClassificationEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "mongrel (Birds)",
                PermissibleValue(text="mongrel (Birds)",
                                 description="mongrel (Birds)") )

class WoolOrHairEnum(EnumDefinitionImpl):

    hair = PermissibleValue(text="hair",
                               description="hair")
    Wool = PermissibleValue(text="Wool",
                               description="Wool")
    wool = PermissibleValue(text="wool",
                               description="wool")
    Hair = PermissibleValue(text="Hair",
                               description="Hair")

    _defn = EnumDefinition(
        name="WoolOrHairEnum",
    )

class WoolTypeEnum(EnumDefinitionImpl):

    medium = PermissibleValue(text="medium",
                                   description="medium")
    Medium = PermissibleValue(text="Medium",
                                   description="Medium")
    Cashmere = PermissibleValue(text="Cashmere",
                                       description="Cashmere")
    cashmere = PermissibleValue(text="cashmere",
                                       description="cashmere")
    Fine = PermissibleValue(text="Fine",
                               description="Fine")
    fine = PermissibleValue(text="fine",
                               description="fine")

    _defn = EnumDefinition(
        name="WoolTypeEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Coarse / Carpet",
                PermissibleValue(text="Coarse / Carpet",
                                 description="Coarse / Carpet") )
        setattr(cls, "mohair/angora",
                PermissibleValue(text="mohair/angora",
                                 description="mohair/angora") )
        setattr(cls, "Mohair / Angora",
                PermissibleValue(text="Mohair / Angora",
                                 description="Mohair / Angora") )
        setattr(cls, "coarse/carpet",
                PermissibleValue(text="coarse/carpet",
                                 description="coarse/carpet") )

class GeographicalClassificationEnum(EnumDefinitionImpl):

    international = PermissibleValue(text="international",
                                                 description="international")
    local = PermissibleValue(text="local",
                                 description="local")
    regional = PermissibleValue(text="regional",
                                       description="regional")

    _defn = EnumDefinition(
        name="GeographicalClassificationEnum",
    )

class LocalCryoConservationStatusEnum(EnumDefinitionImpl):

    Sufficient = PermissibleValue(text="Sufficient",
                                           description="Sufficient")

    _defn = EnumDefinition(
        name="LocalCryoConservationStatusEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "No Information",
                PermissibleValue(text="No Information",
                                 description="No Information") )
        setattr(cls, "No Material",
                PermissibleValue(text="No Material",
                                 description="No Material") )
        setattr(cls, "Not Sufficient",
                PermissibleValue(text="Not Sufficient",
                                 description="Not Sufficient") )

class LocalRiskEnum(EnumDefinitionImpl):

    notAtRisk = PermissibleValue(text="notAtRisk",
                                         description="notAtRisk")
    extinct = PermissibleValue(text="extinct",
                                     description="extinct")
    atRisk = PermissibleValue(text="atRisk",
                                   description="atRisk")
    cryoConservedOnly = PermissibleValue(text="cryoConservedOnly",
                                                         description="cryoConservedOnly")
    unknown = PermissibleValue(text="unknown",
                                     description="unknown")

    _defn = EnumDefinition(
        name="LocalRiskEnum",
    )

class DetailedLocalRiskStatusEnum(EnumDefinitionImpl):

    endangered = PermissibleValue(text="endangered",
                                           description="endangered")
    vulnerable = PermissibleValue(text="vulnerable",
                                           description="vulnerable")
    notAtRisk = PermissibleValue(text="notAtRisk",
                                         description="notAtRisk")
    extinct = PermissibleValue(text="extinct",
                                     description="extinct")
    endangeredMaintained = PermissibleValue(text="endangeredMaintained",
                                                               description="endangeredMaintained")
    critical = PermissibleValue(text="critical",
                                       description="critical")
    cryoConservedOnly = PermissibleValue(text="cryoConservedOnly",
                                                         description="cryoConservedOnly")
    unknown = PermissibleValue(text="unknown",
                                     description="unknown")
    criticalMaintained = PermissibleValue(text="criticalMaintained",
                                                           description="criticalMaintained")

    _defn = EnumDefinition(
        name="DetailedLocalRiskStatusEnum",
    )

class RegionalTransboundaryRisk(detailed)Enum(EnumDefinitionImpl):

    endangered = PermissibleValue(text="endangered",
                                           description="endangered")
    vulnerable = PermissibleValue(text="vulnerable",
                                           description="vulnerable")
    notAtRisk = PermissibleValue(text="notAtRisk",
                                         description="notAtRisk")
    extinct = PermissibleValue(text="extinct",
                                     description="extinct")
    critical = PermissibleValue(text="critical",
                                       description="critical")
    unknown = PermissibleValue(text="unknown",
                                     description="unknown")

    _defn = EnumDefinition(
        name="RegionalTransboundaryRisk(detailed)Enum",
    )

class InternationalTransboundaryRisk(detailed)Enum(EnumDefinitionImpl):

    endangered = PermissibleValue(text="endangered",
                                           description="endangered")
    vulnerable = PermissibleValue(text="vulnerable",
                                           description="vulnerable")
    notAtRisk = PermissibleValue(text="notAtRisk",
                                         description="notAtRisk")
    critical = PermissibleValue(text="critical",
                                       description="critical")
    unknown = PermissibleValue(text="unknown",
                                     description="unknown")

    _defn = EnumDefinition(
        name="InternationalTransboundaryRisk(detailed)Enum",
    )

class UnitOfMeasurementEnum(EnumDefinitionImpl):

    PERCENT = PermissibleValue(text="PERCENT",
                                     description="PERCENT")

    _defn = EnumDefinition(
        name="UnitOfMeasurementEnum",
    )

class NatureEnum(EnumDefinitionImpl):

    NA = PermissibleValue(text="NA",
                           description="NA")
    G = PermissibleValue(text="G",
                         description="G")
    C = PermissibleValue(text="C",
                         description="C")
    E = PermissibleValue(text="E",
                         description="E")

    _defn = EnumDefinition(
        name="NatureEnum",
    )

class ReportingTypeEnum(EnumDefinitionImpl):

    R = PermissibleValue(text="R",
                         description="R")
    G = PermissibleValue(text="G",
                         description="G")
    N = PermissibleValue(text="N",
                         description="N")

    _defn = EnumDefinition(
        name="ReportingTypeEnum",
    )

class M49Level-1RegionEnum(EnumDefinitionImpl):

    Africa = PermissibleValue(text="Africa",
                                   description="Africa")
    Americas = PermissibleValue(text="Americas",
                                       description="Americas")

    _defn = EnumDefinition(
        name="M49Level-1RegionEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Oceania (M49)",
                PermissibleValue(text="Oceania (M49)",
                                 description="Oceania (M49)") )
        setattr(cls, "Europe (M49)",
                PermissibleValue(text="Europe (M49)",
                                 description="Europe (M49)") )
        setattr(cls, "Asia (M49)",
                PermissibleValue(text="Asia (M49)",
                                 description="Asia (M49)") )

class M49IntermediateNameEnum(EnumDefinitionImpl):

    _defn = EnumDefinition(
        name="M49IntermediateNameEnum",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "Middle Africa (M49)",
                PermissibleValue(text="Middle Africa (M49)",
                                 description="Middle Africa (M49)") )
        setattr(cls, "Central America (M49)",
                PermissibleValue(text="Central America (M49)",
                                 description="Central America (M49)") )
        setattr(cls, "Eastern Africa (M49)",
                PermissibleValue(text="Eastern Africa (M49)",
                                 description="Eastern Africa (M49)") )
        setattr(cls, "Southern Africa (M49)",
                PermissibleValue(text="Southern Africa (M49)",
                                 description="Southern Africa (M49)") )
        setattr(cls, "Caribbean (M49)",
                PermissibleValue(text="Caribbean (M49)",
                                 description="Caribbean (M49)") )
        setattr(cls, "South America (M49)",
                PermissibleValue(text="South America (M49)",
                                 description="South America (M49)") )
        setattr(cls, "Western Africa (M49)",
                PermissibleValue(text="Western Africa (M49)",
                                 description="Western Africa (M49)") )

# Slots
class slots:
    pass

slots.Country = Slot(uri=EXAMPLE.Country, name="Country", curie=EXAMPLE.curie('Country'),
                   model_uri=EXAMPLE.Country, domain=None, range=Optional[str])

slots.ISO3 = Slot(uri=EXAMPLE.ISO3, name="ISO3", curie=EXAMPLE.curie('ISO3'),
                   model_uri=EXAMPLE.ISO3, domain=None, range=Optional[str])

slots.Specie = Slot(uri=EXAMPLE.Specie, name="Specie", curie=EXAMPLE.curie('Specie'),
                   model_uri=EXAMPLE.Specie, domain=None, range=Optional[Union[str, "SpecieEnum"]])

slots.Breed = Slot(uri=EXAMPLE.Breed, name="Breed", curie=EXAMPLE.curie('Breed'),
                   model_uri=EXAMPLE.Breed, domain=None, range=Optional[str])

slots.Description_Of_Specific_Uses = Slot(uri=EXAMPLE.Description_Of_Specific_Uses, name="Description Of Specific Uses", curie=EXAMPLE.curie('Description_Of_Specific_Uses'),
                   model_uri=EXAMPLE.Description_Of_Specific_Uses, domain=None, range=Optional[str])

slots.Lang = Slot(uri=EXAMPLE.Lang, name="Lang", curie=EXAMPLE.curie('Lang'),
                   model_uri=EXAMPLE.Lang, domain=None, range=Optional[str])

slots.Description = Slot(uri=EXAMPLE.Description, name="Description", curie=EXAMPLE.curie('Description'),
                   model_uri=EXAMPLE.Description, domain=None, range=Optional[str])

slots.Transboundary_name = Slot(uri=EXAMPLE.Transboundary_name, name="Transboundary name", curie=EXAMPLE.curie('Transboundary_name'),
                   model_uri=EXAMPLE.Transboundary_name, domain=None, range=Optional[Union[str, List[str]]])

slots.Other_name = Slot(uri=EXAMPLE.Other_name, name="Other name", curie=EXAMPLE.curie('Other_name'),
                   model_uri=EXAMPLE.Other_name, domain=None, range=Optional[str])

slots.Uses = Slot(uri=EXAMPLE.Uses, name="Uses", curie=EXAMPLE.curie('Uses'),
                   model_uri=EXAMPLE.Uses, domain=None, range=Optional[str])

slots.Additional_information = Slot(uri=EXAMPLE.Additional_information, name="Additional information", curie=EXAMPLE.curie('Additional_information'),
                   model_uri=EXAMPLE.Additional_information, domain=None, range=Optional[str])

slots.Additional_information_comments = Slot(uri=EXAMPLE.Additional_information_comments, name="Additional information comments", curie=EXAMPLE.curie('Additional_information_comments'),
                   model_uri=EXAMPLE.Additional_information_comments, domain=None, range=Optional[str])

slots.Efabis_cultural_role_comment = Slot(uri=EXAMPLE.Efabis_cultural_role_comment, name="Efabis cultural role comment", curie=EXAMPLE.curie('Efabis_cultural_role_comment'),
                   model_uri=EXAMPLE.Efabis_cultural_role_comment, domain=None, range=Optional[str])

slots.Efabis_cultural_value = Slot(uri=EXAMPLE.Efabis_cultural_value, name="Efabis cultural value", curie=EXAMPLE.curie('Efabis_cultural_value'),
                   model_uri=EXAMPLE.Efabis_cultural_value, domain=None, range=Optional[str])

slots.Adaptability_to_specific_environment = Slot(uri=EXAMPLE.Adaptability_to_specific_environment, name="Adaptability to specific environment", curie=EXAMPLE.curie('Adaptability_to_specific_environment'),
                   model_uri=EXAMPLE.Adaptability_to_specific_environment, domain=None, range=Optional[str])

slots.Specific_resistance_or_tolerance = Slot(uri=EXAMPLE.Specific_resistance_or_tolerance, name="Specific resistance or tolerance", curie=EXAMPLE.curie('Specific_resistance_or_tolerance'),
                   model_uri=EXAMPLE.Specific_resistance_or_tolerance, domain=None, range=Optional[str])

slots.Specific_reproductive_characteristic = Slot(uri=EXAMPLE.Specific_reproductive_characteristic, name="Specific reproductive characteristic", curie=EXAMPLE.curie('Specific_reproductive_characteristic'),
                   model_uri=EXAMPLE.Specific_reproductive_characteristic, domain=None, range=Optional[str])

slots.Special_characteristic_of_product = Slot(uri=EXAMPLE.Special_characteristic_of_product, name="Special characteristic of product", curie=EXAMPLE.curie('Special_characteristic_of_product'),
                   model_uri=EXAMPLE.Special_characteristic_of_product, domain=None, range=Optional[str])

slots.Other_special_qualities = Slot(uri=EXAMPLE.Other_special_qualities, name="Other special qualities", curie=EXAMPLE.curie('Other_special_qualities'),
                   model_uri=EXAMPLE.Other_special_qualities, domain=None, range=Optional[str])

slots.Reference_for_special_qualities = Slot(uri=EXAMPLE.Reference_for_special_qualities, name="Reference for special qualities", curie=EXAMPLE.curie('Reference_for_special_qualities'),
                   model_uri=EXAMPLE.Reference_for_special_qualities, domain=None, range=Optional[str])

slots.Efabis_genetic_features = Slot(uri=EXAMPLE.Efabis_genetic_features, name="Efabis genetic features", curie=EXAMPLE.curie('Efabis_genetic_features'),
                   model_uri=EXAMPLE.Efabis_genetic_features, domain=None, range=Optional[str])

slots.Efabis_environmental_role = Slot(uri=EXAMPLE.Efabis_environmental_role, name="Efabis environmental role", curie=EXAMPLE.curie('Efabis_environmental_role'),
                   model_uri=EXAMPLE.Efabis_environmental_role, domain=None, range=Optional[str])

slots.Efabis_adaptability_to_marginal_land = Slot(uri=EXAMPLE.Efabis_adaptability_to_marginal_land, name="Efabis adaptability to marginal land", curie=EXAMPLE.curie('Efabis_adaptability_to_marginal_land'),
                   model_uri=EXAMPLE.Efabis_adaptability_to_marginal_land, domain=None, range=Optional[str])

slots.Body_conformation = Slot(uri=EXAMPLE.Body_conformation, name="Body conformation", curie=EXAMPLE.curie('Body_conformation'),
                   model_uri=EXAMPLE.Body_conformation, domain=None, range=Optional[str])

slots.Coat_description = Slot(uri=EXAMPLE.Coat_description, name="Coat description", curie=EXAMPLE.curie('Coat_description'),
                   model_uri=EXAMPLE.Coat_description, domain=None, range=Optional[str])

slots.Coat_quality = Slot(uri=EXAMPLE.Coat_quality, name="Coat quality", curie=EXAMPLE.curie('Coat_quality'),
                   model_uri=EXAMPLE.Coat_quality, domain=None, range=Optional[str])

slots.Comb_type = Slot(uri=EXAMPLE.Comb_type, name="Comb type", curie=EXAMPLE.curie('Comb_type'),
                   model_uri=EXAMPLE.Comb_type, domain=None, range=Optional[Union[str, "CombTypeEnum"]])

slots.Skin_colour = Slot(uri=EXAMPLE.Skin_colour, name="Skin colour", curie=EXAMPLE.curie('Skin_colour'),
                   model_uri=EXAMPLE.Skin_colour, domain=None, range=Optional[Union[str, "SkinColourEnum"]])

slots.Shank_and_foot_colour = Slot(uri=EXAMPLE.Shank_and_foot_colour, name="Shank and foot colour", curie=EXAMPLE.curie('Shank_and_foot_colour'),
                   model_uri=EXAMPLE.Shank_and_foot_colour, domain=None, range=Optional[Union[str, "ShankAndFootColourEnum"]])

slots.Plumage_colour = Slot(uri=EXAMPLE.Plumage_colour, name="Plumage colour", curie=EXAMPLE.curie('Plumage_colour'),
                   model_uri=EXAMPLE.Plumage_colour, domain=None, range=Optional[Union[str, "PlumageColourEnum"]])

slots.Pattern_within_feather = Slot(uri=EXAMPLE.Pattern_within_feather, name="Pattern within feather", curie=EXAMPLE.curie('Pattern_within_feather'),
                   model_uri=EXAMPLE.Pattern_within_feather, domain=None, range=Optional[Union[str, "PatternWithinFeatherEnum"]])

slots.Avian_classification = Slot(uri=EXAMPLE.Avian_classification, name="Avian classification", curie=EXAMPLE.curie('Avian_classification'),
                   model_uri=EXAMPLE.Avian_classification, domain=None, range=Optional[Union[str, "AvianClassificationEnum"]])

slots.Color_comments = Slot(uri=EXAMPLE.Color_comments, name="Color comments", curie=EXAMPLE.curie('Color_comments'),
                   model_uri=EXAMPLE.Color_comments, domain=None, range=Optional[str])

slots.Efabis_main_colour = Slot(uri=EXAMPLE.Efabis_main_colour, name="Efabis main colour", curie=EXAMPLE.curie('Efabis_main_colour'),
                   model_uri=EXAMPLE.Efabis_main_colour, domain=None, range=Optional[str])

slots.Efabis_skin_colour = Slot(uri=EXAMPLE.Efabis_skin_colour, name="Efabis skin colour", curie=EXAMPLE.curie('Efabis_skin_colour'),
                   model_uri=EXAMPLE.Efabis_skin_colour, domain=None, range=Optional[str])

slots.Number_of_horns_males = Slot(uri=EXAMPLE.Number_of_horns_males, name="Number of horns males", curie=EXAMPLE.curie('Number_of_horns_males'),
                   model_uri=EXAMPLE.Number_of_horns_males, domain=None, range=Optional[Union[str, "NumberOfHornsMalesEnum"]])

slots.Number_of_horns_females = Slot(uri=EXAMPLE.Number_of_horns_females, name="Number of horns females", curie=EXAMPLE.curie('Number_of_horns_females'),
                   model_uri=EXAMPLE.Number_of_horns_females, domain=None, range=Optional[Union[str, "NumberOfHornsFemalesEnum"]])

slots.Horn_shape_size_and_comments = Slot(uri=EXAMPLE.Horn_shape_size_and_comments, name="Horn shape size and comments", curie=EXAMPLE.curie('Horn_shape_size_and_comments'),
                   model_uri=EXAMPLE.Horn_shape_size_and_comments, domain=None, range=Optional[str])

slots.Wither_height_males = Slot(uri=EXAMPLE.Wither_height_males, name="Wither height males", curie=EXAMPLE.curie('Wither_height_males'),
                   model_uri=EXAMPLE.Wither_height_males, domain=None, range=Optional[float])

slots.Wither_height_females = Slot(uri=EXAMPLE.Wither_height_females, name="Wither height females", curie=EXAMPLE.curie('Wither_height_females'),
                   model_uri=EXAMPLE.Wither_height_females, domain=None, range=Optional[float])

slots.Weight_males = Slot(uri=EXAMPLE.Weight_males, name="Weight males", curie=EXAMPLE.curie('Weight_males'),
                   model_uri=EXAMPLE.Weight_males, domain=None, range=Optional[float])

slots.Weight_females = Slot(uri=EXAMPLE.Weight_females, name="Weight females", curie=EXAMPLE.curie('Weight_females'),
                   model_uri=EXAMPLE.Weight_females, domain=None, range=Optional[float])

slots.Other_specific_visible_traits = Slot(uri=EXAMPLE.Other_specific_visible_traits, name="Other specific visible traits", curie=EXAMPLE.curie('Other_specific_visible_traits'),
                   model_uri=EXAMPLE.Other_specific_visible_traits, domain=None, range=Optional[str])

slots.Breed_classification = Slot(uri=EXAMPLE.Breed_classification, name="Breed classification", curie=EXAMPLE.curie('Breed_classification'),
                   model_uri=EXAMPLE.Breed_classification, domain=None, range=Optional[Union[str, "BreedClassificationEnum"]])

slots.Herdbook = Slot(uri=EXAMPLE.Herdbook, name="Herdbook", curie=EXAMPLE.curie('Herdbook'),
                   model_uri=EXAMPLE.Herdbook, domain=None, range=Optional[Union[str, "HerdbookEnum"]])

slots.Herdbook_established = Slot(uri=EXAMPLE.Herdbook_established, name="Herdbook established", curie=EXAMPLE.curie('Herdbook_established'),
                   model_uri=EXAMPLE.Herdbook_established, domain=None, range=Optional[str])

slots.Domestication_status = Slot(uri=EXAMPLE.Domestication_status, name="Domestication status", curie=EXAMPLE.curie('Domestication_status'),
                   model_uri=EXAMPLE.Domestication_status, domain=None, range=Optional[Union[str, "DomesticationStatusEnum"]])

slots.Taxonomic_classification = Slot(uri=EXAMPLE.Taxonomic_classification, name="Taxonomic classification", curie=EXAMPLE.curie('Taxonomic_classification'),
                   model_uri=EXAMPLE.Taxonomic_classification, domain=None, range=Optional[Union[str, "TaxonomicClassificationEnum"]])

slots.Description_of_origin = Slot(uri=EXAMPLE.Description_of_origin, name="Description of origin", curie=EXAMPLE.curie('Description_of_origin'),
                   model_uri=EXAMPLE.Description_of_origin, domain=None, range=Optional[str])

slots.Year_of_origin = Slot(uri=EXAMPLE.Year_of_origin, name="Year of origin", curie=EXAMPLE.curie('Year_of_origin'),
                   model_uri=EXAMPLE.Year_of_origin, domain=None, range=Optional[str])

slots.Import = Slot(uri=EXAMPLE.Import, name="Import", curie=EXAMPLE.curie('Import'),
                   model_uri=EXAMPLE.Import, domain=None, range=Optional[str])

slots.Location_within_country = Slot(uri=EXAMPLE.Location_within_country, name="Location within country", curie=EXAMPLE.curie('Location_within_country'),
                   model_uri=EXAMPLE.Location_within_country, domain=None, range=Optional[str])

slots.Eggs_per_year_AVG = Slot(uri=EXAMPLE.Eggs_per_year_AVG, name="Eggs per year AVG", curie=EXAMPLE.curie('Eggs_per_year_AVG'),
                   model_uri=EXAMPLE.Eggs_per_year_AVG, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.Eggs_per_year_MIN = Slot(uri=EXAMPLE.Eggs_per_year_MIN, name="Eggs per year MIN", curie=EXAMPLE.curie('Eggs_per_year_MIN'),
                   model_uri=EXAMPLE.Eggs_per_year_MIN, domain=None, range=Optional[int])

slots.Eggs_per_year_MAX = Slot(uri=EXAMPLE.Eggs_per_year_MAX, name="Eggs per year MAX", curie=EXAMPLE.curie('Eggs_per_year_MAX'),
                   model_uri=EXAMPLE.Eggs_per_year_MAX, domain=None, range=Optional[int])

slots.Egg_weight = Slot(uri=EXAMPLE.Egg_weight, name="Egg weight", curie=EXAMPLE.curie('Egg_weight'),
                   model_uri=EXAMPLE.Egg_weight, domain=None, range=Optional[float])

slots.Wool_or_hair = Slot(uri=EXAMPLE.Wool_or_hair, name="Wool or hair", curie=EXAMPLE.curie('Wool_or_hair'),
                   model_uri=EXAMPLE.Wool_or_hair, domain=None, range=Optional[Union[str, "WoolOrHairEnum"]])

slots.Wool_type = Slot(uri=EXAMPLE.Wool_type, name="Wool type", curie=EXAMPLE.curie('Wool_type'),
                   model_uri=EXAMPLE.Wool_type, domain=None, range=Optional[Union[str, "WoolTypeEnum"]])

slots.Fleece_weight_AVG = Slot(uri=EXAMPLE.Fleece_weight_AVG, name="Fleece weight AVG", curie=EXAMPLE.curie('Fleece_weight_AVG'),
                   model_uri=EXAMPLE.Fleece_weight_AVG, domain=None, range=Optional[float])

slots.Fleece_weight_MIN = Slot(uri=EXAMPLE.Fleece_weight_MIN, name="Fleece weight MIN", curie=EXAMPLE.curie('Fleece_weight_MIN'),
                   model_uri=EXAMPLE.Fleece_weight_MIN, domain=None, range=Optional[float])

slots.Fleece_weight_MAX = Slot(uri=EXAMPLE.Fleece_weight_MAX, name="Fleece weight MAX", curie=EXAMPLE.curie('Fleece_weight_MAX'),
                   model_uri=EXAMPLE.Fleece_weight_MAX, domain=None, range=Optional[float])

slots.Fibre_diam = Slot(uri=EXAMPLE.Fibre_diam, name="Fibre diam", curie=EXAMPLE.curie('Fibre_diam'),
                   model_uri=EXAMPLE.Fibre_diam, domain=None, range=Optional[float])

slots.Management_system = Slot(uri=EXAMPLE.Management_system, name="Management system", curie=EXAMPLE.curie('Management_system'),
                   model_uri=EXAMPLE.Management_system, domain=None, range=Optional[str])

slots.Feeding_of_adults = Slot(uri=EXAMPLE.Feeding_of_adults, name="Feeding of adults", curie=EXAMPLE.curie('Feeding_of_adults'),
                   model_uri=EXAMPLE.Feeding_of_adults, domain=None, range=Optional[str])

slots.Mobility = Slot(uri=EXAMPLE.Mobility, name="Mobility", curie=EXAMPLE.curie('Mobility'),
                   model_uri=EXAMPLE.Mobility, domain=None, range=Optional[str])

slots.Milk_per_year_AVG = Slot(uri=EXAMPLE.Milk_per_year_AVG, name="Milk per year AVG", curie=EXAMPLE.curie('Milk_per_year_AVG'),
                   model_uri=EXAMPLE.Milk_per_year_AVG, domain=None, range=Optional[float])

slots.Milk_per_year_MIN = Slot(uri=EXAMPLE.Milk_per_year_MIN, name="Milk per year MIN", curie=EXAMPLE.curie('Milk_per_year_MIN'),
                   model_uri=EXAMPLE.Milk_per_year_MIN, domain=None, range=Optional[int])

slots.Milk_per_year_MAX = Slot(uri=EXAMPLE.Milk_per_year_MAX, name="Milk per year MAX", curie=EXAMPLE.curie('Milk_per_year_MAX'),
                   model_uri=EXAMPLE.Milk_per_year_MAX, domain=None, range=Optional[int])

slots.Lactation_length_AVG = Slot(uri=EXAMPLE.Lactation_length_AVG, name="Lactation length AVG", curie=EXAMPLE.curie('Lactation_length_AVG'),
                   model_uri=EXAMPLE.Lactation_length_AVG, domain=None, range=Optional[float])

slots.Lactation_length_MIN = Slot(uri=EXAMPLE.Lactation_length_MIN, name="Lactation length MIN", curie=EXAMPLE.curie('Lactation_length_MIN'),
                   model_uri=EXAMPLE.Lactation_length_MIN, domain=None, range=Optional[int])

slots.Lactation_length_MAX = Slot(uri=EXAMPLE.Lactation_length_MAX, name="Lactation length MAX", curie=EXAMPLE.curie('Lactation_length_MAX'),
                   model_uri=EXAMPLE.Lactation_length_MAX, domain=None, range=Optional[int])

slots.Milk_yield_per_lactation_(kg)_AVG = Slot(uri=EXAMPLE['Milk_yield_per_lactation_(kg)_AVG'], name="Milk yield per lactation (kg) AVG", curie=EXAMPLE.curie('Milk_yield_per_lactation_(kg)_AVG'),
                   model_uri=EXAMPLE['Milk_yield_per_lactation_(kg)_AVG'], domain=None, range=Optional[float])

slots.Milk_yield_per_lactation_(kg)_MIN = Slot(uri=EXAMPLE['Milk_yield_per_lactation_(kg)_MIN'], name="Milk yield per lactation (kg) MIN", curie=EXAMPLE.curie('Milk_yield_per_lactation_(kg)_MIN'),
                   model_uri=EXAMPLE['Milk_yield_per_lactation_(kg)_MIN'], domain=None, range=Optional[float])

slots.Milk_yield_per_lactation_(kg)_MAX = Slot(uri=EXAMPLE['Milk_yield_per_lactation_(kg)_MAX'], name="Milk yield per lactation (kg) MAX", curie=EXAMPLE.curie('Milk_yield_per_lactation_(kg)_MAX'),
                   model_uri=EXAMPLE['Milk_yield_per_lactation_(kg)_MAX'], domain=None, range=Optional[float])

slots.Milk_fat_AVG = Slot(uri=EXAMPLE.Milk_fat_AVG, name="Milk fat AVG", curie=EXAMPLE.curie('Milk_fat_AVG'),
                   model_uri=EXAMPLE.Milk_fat_AVG, domain=None, range=Optional[float])

slots.Milk_fat_MIN = Slot(uri=EXAMPLE.Milk_fat_MIN, name="Milk fat MIN", curie=EXAMPLE.curie('Milk_fat_MIN'),
                   model_uri=EXAMPLE.Milk_fat_MIN, domain=None, range=Optional[float])

slots.Milk_fat_MAX = Slot(uri=EXAMPLE.Milk_fat_MAX, name="Milk fat MAX", curie=EXAMPLE.curie('Milk_fat_MAX'),
                   model_uri=EXAMPLE.Milk_fat_MAX, domain=None, range=Optional[float])

slots.Milk_per_day = Slot(uri=EXAMPLE.Milk_per_day, name="Milk per day", curie=EXAMPLE.curie('Milk_per_day'),
                   model_uri=EXAMPLE.Milk_per_day, domain=None, range=Optional[float])

slots.Number_of_lactations = Slot(uri=EXAMPLE.Number_of_lactations, name="Number of lactations", curie=EXAMPLE.curie('Number_of_lactations'),
                   model_uri=EXAMPLE.Number_of_lactations, domain=None, range=Optional[float])

slots.Efabis_milk_protein_AVG = Slot(uri=EXAMPLE.Efabis_milk_protein_AVG, name="Efabis milk protein AVG", curie=EXAMPLE.curie('Efabis_milk_protein_AVG'),
                   model_uri=EXAMPLE.Efabis_milk_protein_AVG, domain=None, range=Optional[float])

slots.Efabis_milk_protein_MIN = Slot(uri=EXAMPLE.Efabis_milk_protein_MIN, name="Efabis milk protein MIN", curie=EXAMPLE.curie('Efabis_milk_protein_MIN'),
                   model_uri=EXAMPLE.Efabis_milk_protein_MIN, domain=None, range=Optional[float])

slots.Efabis_milk_protein_MAX = Slot(uri=EXAMPLE.Efabis_milk_protein_MAX, name="Efabis milk protein MAX", curie=EXAMPLE.curie('Efabis_milk_protein_MAX'),
                   model_uri=EXAMPLE.Efabis_milk_protein_MAX, domain=None, range=Optional[float])

slots.Birth_weight_males = Slot(uri=EXAMPLE.Birth_weight_males, name="Birth weight males", curie=EXAMPLE.curie('Birth_weight_males'),
                   model_uri=EXAMPLE.Birth_weight_males, domain=None, range=Optional[float])

slots.Birth_weight_females = Slot(uri=EXAMPLE.Birth_weight_females, name="Birth weight females", curie=EXAMPLE.curie('Birth_weight_females'),
                   model_uri=EXAMPLE.Birth_weight_females, domain=None, range=Optional[float])

slots.Age_maturity_males = Slot(uri=EXAMPLE.Age_maturity_males, name="Age maturity males", curie=EXAMPLE.curie('Age_maturity_males'),
                   model_uri=EXAMPLE.Age_maturity_males, domain=None, range=Optional[float])

slots.Age_maturity_females = Slot(uri=EXAMPLE.Age_maturity_females, name="Age maturity females", curie=EXAMPLE.curie('Age_maturity_females'),
                   model_uri=EXAMPLE.Age_maturity_females, domain=None, range=Optional[float])

slots.Age_breeding_males = Slot(uri=EXAMPLE.Age_breeding_males, name="Age breeding males", curie=EXAMPLE.curie('Age_breeding_males'),
                   model_uri=EXAMPLE.Age_breeding_males, domain=None, range=Optional[float])

slots.Age_breeding_females = Slot(uri=EXAMPLE.Age_breeding_females, name="Age breeding females", curie=EXAMPLE.curie('Age_breeding_females'),
                   model_uri=EXAMPLE.Age_breeding_females, domain=None, range=Optional[float])

slots.Age_first_parturition_AVG = Slot(uri=EXAMPLE.Age_first_parturition_AVG, name="Age first parturition AVG", curie=EXAMPLE.curie('Age_first_parturition_AVG'),
                   model_uri=EXAMPLE.Age_first_parturition_AVG, domain=None, range=Optional[float])

slots.Age_first_parturition_MIN = Slot(uri=EXAMPLE.Age_first_parturition_MIN, name="Age first parturition MIN", curie=EXAMPLE.curie('Age_first_parturition_MIN'),
                   model_uri=EXAMPLE.Age_first_parturition_MIN, domain=None, range=Optional[float])

slots.Age_first_parturition_MAX = Slot(uri=EXAMPLE.Age_first_parturition_MAX, name="Age first parturition MAX", curie=EXAMPLE.curie('Age_first_parturition_MAX'),
                   model_uri=EXAMPLE.Age_first_parturition_MAX, domain=None, range=Optional[float])

slots.Parturition_interval_AVG = Slot(uri=EXAMPLE.Parturition_interval_AVG, name="Parturition interval AVG", curie=EXAMPLE.curie('Parturition_interval_AVG'),
                   model_uri=EXAMPLE.Parturition_interval_AVG, domain=None, range=Optional[float])

slots.Parturition_interval_MIN = Slot(uri=EXAMPLE.Parturition_interval_MIN, name="Parturition interval MIN", curie=EXAMPLE.curie('Parturition_interval_MIN'),
                   model_uri=EXAMPLE.Parturition_interval_MIN, domain=None, range=Optional[int])

slots.Parturition_interval_MAX = Slot(uri=EXAMPLE.Parturition_interval_MAX, name="Parturition interval MAX", curie=EXAMPLE.curie('Parturition_interval_MAX'),
                   model_uri=EXAMPLE.Parturition_interval_MAX, domain=None, range=Optional[int])

slots.Length_productive_life = Slot(uri=EXAMPLE.Length_productive_life, name="Length productive life", curie=EXAMPLE.curie('Length_productive_life'),
                   model_uri=EXAMPLE.Length_productive_life, domain=None, range=Optional[float])

slots.Daily_gain = Slot(uri=EXAMPLE.Daily_gain, name="Daily gain", curie=EXAMPLE.curie('Daily_gain'),
                   model_uri=EXAMPLE.Daily_gain, domain=None, range=Optional[float])

slots.Carcass_weight = Slot(uri=EXAMPLE.Carcass_weight, name="Carcass weight", curie=EXAMPLE.curie('Carcass_weight'),
                   model_uri=EXAMPLE.Carcass_weight, domain=None, range=Optional[float])

slots.Dressing_percentage = Slot(uri=EXAMPLE.Dressing_percentage, name="Dressing percentage", curie=EXAMPLE.curie('Dressing_percentage'),
                   model_uri=EXAMPLE.Dressing_percentage, domain=None, range=Optional[float])

slots.Performance_data_reference = Slot(uri=EXAMPLE.Performance_data_reference, name="Performance data reference", curie=EXAMPLE.curie('Performance_data_reference'),
                   model_uri=EXAMPLE.Performance_data_reference, domain=None, range=Optional[str])

slots.Managment_conditions_performance_measured = Slot(uri=EXAMPLE.Managment_conditions_performance_measured, name="Managment conditions performance measured", curie=EXAMPLE.curie('Managment_conditions_performance_measured'),
                   model_uri=EXAMPLE.Managment_conditions_performance_measured, domain=None, range=Optional[str])

slots.Comments_managment_conditions = Slot(uri=EXAMPLE.Comments_managment_conditions, name="Comments managment conditions", curie=EXAMPLE.curie('Comments_managment_conditions'),
                   model_uri=EXAMPLE.Comments_managment_conditions, domain=None, range=Optional[str])

slots.Additional_performance_parameters = Slot(uri=EXAMPLE.Additional_performance_parameters, name="Additional performance parameters", curie=EXAMPLE.curie('Additional_performance_parameters'),
                   model_uri=EXAMPLE.Additional_performance_parameters, domain=None, range=Optional[str])

slots.Litter_size_AVG = Slot(uri=EXAMPLE.Litter_size_AVG, name="Litter size AVG", curie=EXAMPLE.curie('Litter_size_AVG'),
                   model_uri=EXAMPLE.Litter_size_AVG, domain=None, range=Optional[float])

slots.Litter_size_MIN = Slot(uri=EXAMPLE.Litter_size_MIN, name="Litter size MIN", curie=EXAMPLE.curie('Litter_size_MIN'),
                   model_uri=EXAMPLE.Litter_size_MIN, domain=None, range=Optional[float])

slots.Litter_size_MAX = Slot(uri=EXAMPLE.Litter_size_MAX, name="Litter size MAX", curie=EXAMPLE.curie('Litter_size_MAX'),
                   model_uri=EXAMPLE.Litter_size_MAX, domain=None, range=Optional[float])

slots.Geographical_classification = Slot(uri=EXAMPLE.Geographical_classification, name="Geographical classification", curie=EXAMPLE.curie('Geographical_classification'),
                   model_uri=EXAMPLE.Geographical_classification, domain=None, range=Optional[Union[str, "GeographicalClassificationEnum"]])

slots.Local_cryo_conservation_status = Slot(uri=EXAMPLE.Local_cryo_conservation_status, name="Local cryo conservation status", curie=EXAMPLE.curie('Local_cryo_conservation_status'),
                   model_uri=EXAMPLE.Local_cryo_conservation_status, domain=None, range=Optional[Union[str, "LocalCryoConservationStatusEnum"]])

slots.Local_Risk = Slot(uri=EXAMPLE.Local_Risk, name="Local Risk", curie=EXAMPLE.curie('Local_Risk'),
                   model_uri=EXAMPLE.Local_Risk, domain=None, range=Optional[Union[str, "LocalRiskEnum"]])

slots.Detailed_local_risk_status = Slot(uri=EXAMPLE.Detailed_local_risk_status, name="Detailed local risk status", curie=EXAMPLE.curie('Detailed_local_risk_status'),
                   model_uri=EXAMPLE.Detailed_local_risk_status, domain=None, range=Optional[Union[str, "DetailedLocalRiskStatusEnum"]])

slots.Regional_Transboundary_Risk_(detailed) = Slot(uri=EXAMPLE['Regional_Transboundary_Risk_(detailed)'], name="Regional Transboundary Risk (detailed)", curie=EXAMPLE.curie('Regional_Transboundary_Risk_(detailed)'),
                   model_uri=EXAMPLE['Regional_Transboundary_Risk_(detailed)'], domain=None, range=Optional[Union[str, "RegionalTransboundaryRisk(detailed)Enum"]])

slots.International_Transboundary_Risk_(detailed) = Slot(uri=EXAMPLE['International_Transboundary_Risk_(detailed)'], name="International Transboundary Risk (detailed)", curie=EXAMPLE.curie('International_Transboundary_Risk_(detailed)'),
                   model_uri=EXAMPLE['International_Transboundary_Risk_(detailed)'], domain=None, range=Optional[Union[str, "InternationalTransboundaryRisk(detailed)Enum"]])

slots.Indicator_Reference_Number = Slot(uri=EXAMPLE.Indicator_Reference_Number, name="Indicator Reference Number", curie=EXAMPLE.curie('Indicator_Reference_Number'),
                   model_uri=EXAMPLE.Indicator_Reference_Number, domain=None, range=Optional[Union[str, XSDDateTime]])

slots.Series_Name = Slot(uri=EXAMPLE.Series_Name, name="Series Name", curie=EXAMPLE.curie('Series_Name'),
                   model_uri=EXAMPLE.Series_Name, domain=None, range=Optional[int])

slots.Series_Description = Slot(uri=EXAMPLE.Series_Description, name="Series Description", curie=EXAMPLE.curie('Series_Description'),
                   model_uri=EXAMPLE.Series_Description, domain=None, range=Optional[str])

slots.Geo_Area_Code = Slot(uri=EXAMPLE.Geo_Area_Code, name="Geo Area Code", curie=EXAMPLE.curie('Geo_Area_Code'),
                   model_uri=EXAMPLE.Geo_Area_Code, domain=None, range=Optional[int])

slots.Geo_Area_Name = Slot(uri=EXAMPLE.Geo_Area_Name, name="Geo Area Name", curie=EXAMPLE.curie('Geo_Area_Name'),
                   model_uri=EXAMPLE.Geo_Area_Name, domain=None, range=Optional[str])

slots.Year = Slot(uri=EXAMPLE.Year, name="Year", curie=EXAMPLE.curie('Year'),
                   model_uri=EXAMPLE.Year, domain=None, range=Optional[int])

slots.Reference_Area_Type_(Countries) = Slot(uri=EXAMPLE['Reference_Area_Type_(Countries)'], name="Reference Area Type (Countries)", curie=EXAMPLE.curie('Reference_Area_Type_(Countries)'),
                   model_uri=EXAMPLE['Reference_Area_Type_(Countries)'], domain=None, range=Optional[str])

slots.Indicator_value = Slot(uri=EXAMPLE.Indicator_value, name="Indicator value", curie=EXAMPLE.curie('Indicator_value'),
                   model_uri=EXAMPLE.Indicator_value, domain=None, range=Optional[str])

slots.Unit_of_Measurement = Slot(uri=EXAMPLE.Unit_of_Measurement, name="Unit of Measurement", curie=EXAMPLE.curie('Unit_of_Measurement'),
                   model_uri=EXAMPLE.Unit_of_Measurement, domain=None, range=Optional[Union[str, "UnitOfMeasurementEnum"]])

slots.Nature = Slot(uri=EXAMPLE.Nature, name="Nature", curie=EXAMPLE.curie('Nature'),
                   model_uri=EXAMPLE.Nature, domain=None, range=Optional[Union[str, "NatureEnum"]])

slots.Reporting_Type = Slot(uri=EXAMPLE.Reporting_Type, name="Reporting Type", curie=EXAMPLE.curie('Reporting_Type'),
                   model_uri=EXAMPLE.Reporting_Type, domain=None, range=Optional[Union[str, "ReportingTypeEnum"]])

slots.Number_of_local_breeds_(not_extinct) = Slot(uri=EXAMPLE['Number_of_local_breeds_(not_extinct)'], name="Number of local breeds (not extinct)", curie=EXAMPLE.curie('Number_of_local_breeds_(not_extinct)'),
                   model_uri=EXAMPLE['Number_of_local_breeds_(not_extinct)'], domain=None, range=Optional[int])

slots.Number_of_local_breeds_with_unknown_status = Slot(uri=EXAMPLE.Number_of_local_breeds_with_unknown_status, name="Number of local breeds with unknown status", curie=EXAMPLE.curie('Number_of_local_breeds_with_unknown_status'),
                   model_uri=EXAMPLE.Number_of_local_breeds_with_unknown_status, domain=None, range=Optional[int])

slots.Number_of_local_breeds_at_risk = Slot(uri=EXAMPLE.Number_of_local_breeds_at_risk, name="Number of local breeds at risk", curie=EXAMPLE.curie('Number_of_local_breeds_at_risk'),
                   model_uri=EXAMPLE.Number_of_local_breeds_at_risk, domain=None, range=Optional[int])

slots.Number_of_local_breeds_not_at_risk = Slot(uri=EXAMPLE.Number_of_local_breeds_not_at_risk, name="Number of local breeds not at risk", curie=EXAMPLE.curie('Number_of_local_breeds_not_at_risk'),
                   model_uri=EXAMPLE.Number_of_local_breeds_not_at_risk, domain=None, range=Optional[int])

slots.Source_Detail = Slot(uri=EXAMPLE.Source_Detail, name="Source Detail", curie=EXAMPLE.curie('Source_Detail'),
                   model_uri=EXAMPLE.Source_Detail, domain=None, range=Optional[Union[str, DAD-IS7.9.2021HttpIdentifier]])

slots.Foot_Notes = Slot(uri=EXAMPLE.Foot_Notes, name="Foot Notes", curie=EXAMPLE.curie('Foot_Notes'),
                   model_uri=EXAMPLE.Foot_Notes, domain=None, range=Optional[str])

slots.SDG_Region_Code = Slot(uri=EXAMPLE.SDG_Region_Code, name="SDG Region Code", curie=EXAMPLE.curie('SDG_Region_Code'),
                   model_uri=EXAMPLE.SDG_Region_Code, domain=None, range=Optional[int])

slots.SDG_Region_Name = Slot(uri=EXAMPLE.SDG_Region_Name, name="SDG Region Name", curie=EXAMPLE.curie('SDG_Region_Name'),
                   model_uri=EXAMPLE.SDG_Region_Name, domain=None, range=Optional[str])

slots.M49_Level_1_Code = Slot(uri=EXAMPLE.M49_Level_1_Code, name="M49 Level-1 Code", curie=EXAMPLE.curie('M49_Level_1_Code'),
                   model_uri=EXAMPLE.M49_Level_1_Code, domain=None, range=Optional[int])

slots.M49_Level_1_Region = Slot(uri=EXAMPLE.M49_Level_1_Region, name="M49 Level-1 Region", curie=EXAMPLE.curie('M49_Level_1_Region'),
                   model_uri=EXAMPLE.M49_Level_1_Region, domain=None, range=Optional[Union[str, "M49Level-1RegionEnum"]])

slots.M49_Level_2_Code = Slot(uri=EXAMPLE.M49_Level_2_Code, name="M49 Level-2 Code", curie=EXAMPLE.curie('M49_Level_2_Code'),
                   model_uri=EXAMPLE.M49_Level_2_Code, domain=None, range=Optional[int])

slots.M49_Level_2_Name = Slot(uri=EXAMPLE.M49_Level_2_Name, name="M49 Level-2 Name", curie=EXAMPLE.curie('M49_Level_2_Name'),
                   model_uri=EXAMPLE.M49_Level_2_Name, domain=None, range=Optional[str])

slots.M49_Intermediate_Code = Slot(uri=EXAMPLE.M49_Intermediate_Code, name="M49 Intermediate Code", curie=EXAMPLE.curie('M49_Intermediate_Code'),
                   model_uri=EXAMPLE.M49_Intermediate_Code, domain=None, range=Optional[int])

slots.M49_Intermediate_Name = Slot(uri=EXAMPLE.M49_Intermediate_Name, name="M49 Intermediate Name", curie=EXAMPLE.curie('M49_Intermediate_Name'),
                   model_uri=EXAMPLE.M49_Intermediate_Name, domain=None, range=Optional[Union[str, "M49IntermediateNameEnum"]])

slots.MDG_Code = Slot(uri=EXAMPLE.MDG_Code, name="MDG Code", curie=EXAMPLE.curie('MDG_Code'),
                   model_uri=EXAMPLE.MDG_Code, domain=None, range=Optional[int])

slots.MDG_Regions = Slot(uri=EXAMPLE.MDG_Regions, name="MDG Regions", curie=EXAMPLE.curie('MDG_Regions'),
                   model_uri=EXAMPLE.MDG_Regions, domain=None, range=Optional[str])

slots.LDCs_Code = Slot(uri=EXAMPLE.LDCs_Code, name="LDCs Code", curie=EXAMPLE.curie('LDCs_Code'),
                   model_uri=EXAMPLE.LDCs_Code, domain=None, range=Optional[int])

slots.LDCs_Name = Slot(uri=EXAMPLE.LDCs_Name, name="LDCs Name", curie=EXAMPLE.curie('LDCs_Name'),
                   model_uri=EXAMPLE.LDCs_Name, domain=None, range=Optional[str])

slots.LLDCs_Code = Slot(uri=EXAMPLE.LLDCs_Code, name="LLDCs Code", curie=EXAMPLE.curie('LLDCs_Code'),
                   model_uri=EXAMPLE.LLDCs_Code, domain=None, range=Optional[int])

slots.LLDCs_Name = Slot(uri=EXAMPLE.LLDCs_Name, name="LLDCs Name", curie=EXAMPLE.curie('LLDCs_Name'),
                   model_uri=EXAMPLE.LLDCs_Name, domain=None, range=Optional[str])

slots.Number_of_countries_or_territories_in_the_region = Slot(uri=EXAMPLE.Number_of_countries_or_territories_in_the_region, name="Number of countries or territories in the region", curie=EXAMPLE.curie('Number_of_countries_or_territories_in_the_region'),
                   model_uri=EXAMPLE.Number_of_countries_or_territories_in_the_region, domain=None, range=Optional[int])

slots.Number_of_countries_or_territories_with_valid_data = Slot(uri=EXAMPLE.Number_of_countries_or_territories_with_valid_data, name="Number of countries or territories with valid data", curie=EXAMPLE.curie('Number_of_countries_or_territories_with_valid_data'),
                   model_uri=EXAMPLE.Number_of_countries_or_territories_with_valid_data, domain=None, range=Optional[int])

slots.Percentage_of_countries_or_territories_with_valid_data = Slot(uri=EXAMPLE.Percentage_of_countries_or_territories_with_valid_data, name="Percentage of countries or territories with valid data", curie=EXAMPLE.curie('Percentage_of_countries_or_territories_with_valid_data'),
                   model_uri=EXAMPLE.Percentage_of_countries_or_territories_with_valid_data, domain=None, range=Optional[float])