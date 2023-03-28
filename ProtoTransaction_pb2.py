# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ProtoTransaction.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ProtoEnum_pb2 as ProtoEnum__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16ProtoTransaction.proto\x12\x0btransaction\x1a\x0fProtoEnum.proto\"\xca\x04\n\x07Payslip\x12\x14\n\x0cmanagerLevel\x18\x01 \x01(\x05\x12\x11\n\tloginDays\x18\x02 \x01(\x05\x12\x13\n\x0b\x61\x62senceDays\x18\x03 \x01(\x05\x12\x13\n\x0b\x62\x61sicSalary\x18\x04 \x01(\x05\x12\x15\n\ractivityHours\x18\x05 \x01(\x05\x12\x15\n\ractivityBonus\x18\x06 \x01(\x05\x12\x17\n\x0fgvgHighestPoint\x18\x07 \x01(\x03\x12\x1c\n\x14gvgHighestPointBonus\x18\x08 \x01(\x05\x12\x16\n\x0etotalCardLevel\x18\t \x01(\x05\x12\x16\n\x0e\x63\x61rdLevelBonus\x18\n \x01(\x05\x12\x16\n\x0etotalFanAmount\x18\x0b \x01(\x03\x12\x16\n\x0e\x66\x61nAmountBonus\x18\x0c \x01(\x05\x12\x1a\n\x12totalFanEventScore\x18\r \x01(\x03\x12\x1a\n\x12\x66\x61nEventScoreBonus\x18\x0e \x01(\x05\x12\x19\n\x11totalContestScore\x18\x0f \x01(\x03\x12\x19\n\x11\x63ontestScoreBonus\x18\x10 \x01(\x05\x12\x12\n\nloginTimes\x18\x11 \x03(\x03\x12\x1c\n\x14mostGrownCharacterId\x18\x12 \x01(\t\x12\x1e\n\x16hierarchyDetailGradeId\x18\x13 \x01(\t\x12\x16\n\x0ehierarchyPoint\x18\x14 \x01(\x03\x12\x1b\n\x13hierarchyGradeBonus\x18\x15 \x01(\x05\x12\x15\n\rhierarchyRank\x18\x16 \x01(\x05\x12\x0c\n\x04year\x18\x17 \x01(\x05\x12\r\n\x05month\x18\x18 \x01(\x05\"\xbb\x05\n\x04User\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nmanagerExp\x18\x02 \x01(\x03\x12\x14\n\x0c\x64\x65\x63kSequence\x18\x03 \x01(\x03\x12\x0f\n\x07guildId\x18\x04 \x01(\t\x12\x1a\n\x12lastGuildCheckTime\x18\x05 \x01(\x03\x12\x12\n\ndivisionId\x18\x06 \x01(\t\x12\x17\n\x0f\x66irstDivisionId\x18\x07 \x01(\t\x12\x10\n\x08\x65mblemId\x18\x08 \x01(\t\x12\x1b\n\x13\x64\x65\x63kMaxOverallValue\x18\t \x01(\x03\x12&\n\x1elastCreatedForumThreadDatetime\x18\n \x01(\x03\x12\x15\n\rgameStartTime\x18\x0b \x01(\x03\x12\x15\n\rlastLoginTime\x18\x0c \x01(\x03\x12\x18\n\x10\x63\x61rdSupportLevel\x18\r \x01(\x05\x12\x1f\n\x17\x63\x61rdSupportReleaseCount\x18\x0e \x01(\x05\x12\x18\n\x10nextPhotoImageId\x18\x0f \x01(\t\x12\x19\n\x11\x64ivisionMovedTime\x18\x10 \x01(\x03\x12\x12\n\nisReviewed\x18\x11 \x01(\x08\x12*\n\"questMainAreaLastClearCharacterIds\x18\x12 \x03(\t\x12\x15\n\rhighestSalary\x18\x13 \x01(\x05\x12\x1b\n\x13tutorialClearedTime\x18\x14 \x01(\x03\x12\x19\n\x11\x63omebackStartTime\x18\x15 \x01(\x03\x12\x1f\n\x17photoLimitExtendedCount\x18\x16 \x01(\x05\x12\x18\n\x10inviteHostUserId\x18\x17 \x01(\t\x12\x13\n\x0b\x62uddyCardId\x18\x18 \x01(\t\x12\x19\n\x11nextPhotoImageIds\x18\x19 \x03(\t\x12\x14\n\x0cmanagerLevel\x18\x64 \x01(\x05\x12\x1c\n\x14\x63\x61rdSupportMaxNumber\x18\x65 \x01(\x05\"4\n\rUserAccessory\x12\x13\n\x0b\x61\x63\x63\x65ssoryId\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"e\n\x08UserArea\x12\x0e\n\x06\x61reaId\x18\x01 \x01(\t\x12\x17\n\x0f\x63learQuestCount\x18\x02 \x01(\x05\x12\x17\n\x0f\x64\x61ilyClearCount\x18\x03 \x01(\x05\x12\x17\n\x0flastClearedTime\x18\x04 \x01(\x03\"\xe5\x07\n\x08UserCard\x12\x0e\n\x06\x63\x61rdId\x18\x01 \x01(\t\x12\x10\n\x08totalExp\x18\x02 \x01(\x03\x12\x16\n\x0erarityTotalExp\x18\x03 \x01(\x05\x12\x13\n\x0bskillLevel1\x18\x04 \x01(\x05\x12\x13\n\x0bskillLevel2\x18\x05 \x01(\x05\x12\x13\n\x0bskillLevel3\x18\x06 \x01(\x05\x12\x18\n\x10liveAbilityLevel\x18\x07 \x01(\x05\x12\x1c\n\x14\x61\x63tivityAbilityLevel\x18\x08 \x01(\x05\x12\x14\n\x0cobtainedTime\x18\t \x01(\x03\x12\x11\n\tsupported\x18\n \x01(\x08\x12\x17\n\x0flastEnhanceTime\x18\x0b \x01(\x03\x12\x14\n\x0crankTotalExp\x18\x0c \x01(\x05\x12/\n\x0b\x64isplayType\x18\r \x01(\x0e\x32\x1a.ProtoEnum.CardDisplayType\x12\r\n\x05level\x18\x64 \x01(\x05\x12\x0e\n\x06rarity\x18\x65 \x01(\x05\x12\r\n\x05vocal\x18\x66 \x01(\x03\x12\r\n\x05\x64\x61nce\x18g \x01(\x03\x12\x0e\n\x06visual\x18h \x01(\x03\x12\x0f\n\x07stamina\x18i \x01(\x03\x12\x0e\n\x06mental\x18j \x01(\x03\x12\x11\n\ttechnique\x18k \x01(\x03\x12\x10\n\x08skillId1\x18l \x01(\t\x12\x10\n\x08skillId2\x18m \x01(\t\x12\x10\n\x08skillId3\x18n \x01(\t\x12\x15\n\rliveAbilityId\x18o \x01(\t\x12\x19\n\x11\x61\x63tivityAbilityId\x18p \x01(\t\x12\x1b\n\x13photoEquipableCount\x18q \x01(\x05\x12\x11\n\tbaseLevel\x18r \x01(\x05\x12\x11\n\tbaseVocal\x18s \x01(\x03\x12\x11\n\tbaseDance\x18t \x01(\x03\x12\x12\n\nbaseVisual\x18u \x01(\x03\x12\x13\n\x0b\x62\x61seStamina\x18v \x01(\x03\x12\x17\n\x0f\x62\x61seSkillLevel1\x18w \x01(\x05\x12\x17\n\x0f\x62\x61seSkillLevel2\x18x \x01(\x05\x12\x17\n\x0f\x62\x61seSkillLevel3\x18y \x01(\x05\x12\x1c\n\x14\x62\x61seLiveAbilityLevel\x18z \x01(\x05\x12 \n\x18\x62\x61seActivityAbilityLevel\x18{ \x01(\x05\x12\x14\n\x0c\x62\x61seSkillId1\x18| \x01(\t\x12\x14\n\x0c\x62\x61seSkillId2\x18} \x01(\t\x12\x14\n\x0c\x62\x61seSkillId3\x18~ \x01(\t\x12\x19\n\x11\x62\x61seLiveAbilityId\x18\x7f \x01(\t\x12\x1e\n\x15\x62\x61seActivityAbilityId\x18\x80\x01 \x01(\t\x12 \n\x17\x62\x61sePhotoEquipableCount\x18\x81\x01 \x01(\x05\x12\r\n\x04rank\x18\x82\x01 \x01(\x05\"\xb2\x03\n\rUserCharacter\x12\x13\n\x0b\x63haracterId\x18\x01 \x01(\t\x12\x13\n\x0b\x61\x63tivityExp\x18\x02 \x01(\x03\x12\x17\n\x0f\x61\x63tivityStamina\x18\x03 \x01(\x05\x12\x16\n\x0elightFanAmount\x18\x04 \x01(\x05\x12\x17\n\x0fmiddleFanAmount\x18\x05 \x01(\x05\x12\x16\n\x0eheavyFanAmount\x18\x06 \x01(\x05\x12\x19\n\x11\x66\x61voriteCostumeId\x18\x07 \x01(\t\x12\x1a\n\x12staminaUpdatedTime\x18\x08 \x01(\x03\x12\x12\n\ninActivity\x18\t \x01(\x08\x12\x13\n\x0breliability\x18\n \x01(\x05\x12\x18\n\x10liveHighestScore\x18\x0b \x01(\x03\x12 \n\x18\x63haracterOnlyPhotoAmount\x18\x0c \x01(\x05\x12\x15\n\rliveCostumeId\x18\r \x01(\t\x12\x16\n\x0e\x66\x61voriteHairId\x18\x0e \x01(\t\x12\x12\n\nliveHairId\x18\x0f \x01(\t\x12\x15\n\ractivityLevel\x18\x64 \x01(\x05\x12\x1f\n\x17\x61udienceCandidateAmount\x18\x65 \x01(\x05\"f\n\x12UserCharacterMusic\x12\x13\n\x0b\x63haracterId\x18\x01 \x01(\t\x12\x0f\n\x07musicId\x18\x02 \x01(\t\x12\x14\n\x0cmasteryPoint\x18\x03 \x01(\x05\x12\x14\n\x0cmasteryLevel\x18\x64 \x01(\x05\"G\n\x0bUserCostume\x12\x11\n\tcostumeId\x18\x01 \x01(\t\x12\x0f\n\x07\x63hecked\x18\x02 \x01(\x08\x12\x14\n\x0cobtainedTime\x18\x03 \x01(\x03\"&\n\x0eUserDecoration\x12\x14\n\x0c\x64\x65\x63orationId\x18\x01 \x01(\t\"\x1e\n\nUserEmblem\x12\x10\n\x08\x65mblemId\x18\x01 \x01(\t\"+\n\x08UserHair\x12\x0e\n\x06hairId\x18\x01 \x01(\t\x12\x0f\n\x07\x63hecked\x18\x02 \x01(\x08\"\xdd\x01\n\rUserHierarchy\x12\x19\n\x11\x62\x65stDetailGradeId\x18\x01 \x01(\t\x12\x19\n\x11\x63urrentFixedPoint\x18\x02 \x01(\x03\x12\x1c\n\x14\x63urrentVariablePoint\x18\x03 \x01(\x03\x12\x16\n\x0e\x62\x65stTotalPoint\x18\x04 \x01(\x03\x12\"\n\x1a\x63urrentPointUpdateDatetime\x18\x05 \x01(\x03\x12\x19\n\x11receivedRewardIds\x18\x06 \x03(\t\x12!\n\x19receivedDivisionRewardIds\x18\x07 \x03(\t\"\x92\x01\n\x10UserHomePosition\x12\x35\n\x10homePositionType\x18\x01 \x01(\x0e\x32\x1b.ProtoEnum.HomePositionType\x12\x13\n\x0b\x63haracterId\x18\x02 \x01(\t\x12\x19\n\x11isCharacterRandom\x18\x03 \x01(\x08\x12\x17\n\x0fisCostumeRandom\x18\x04 \x01(\x08\"\"\n\x0cUserHomeTalk\x12\x12\n\nhomeTalkId\x18\x01 \x01(\t\"?\n\x08UserItem\x12\x0e\n\x06itemId\x18\x01 \x01(\t\x12\x13\n\x0b\x65xpiredTime\x18\x02 \x01(\x03\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"\x81\x01\n\x0eUserLoginBonus\x12\x14\n\x0cloginBonusId\x18\x01 \x01(\t\x12\x15\n\rlastLoginTime\x18\x02 \x01(\x03\x12\x12\n\nloginCount\x18\x03 \x01(\x05\x12\x14\n\x0creceiveCount\x18\x04 \x01(\x05\x12\x18\n\x10loginBonusTextId\x18\x05 \x01(\t\"\x8e\x01\n\x0bUserMessage\x12\x11\n\tmessageId\x18\x01 \x01(\t\x12\x37\n\x11messageStatusType\x18\x02 \x01(\x0e\x32\x1c.ProtoEnum.MessageStatusType\x12\x1e\n\x16selectMessageDetailIds\x18\x03 \x03(\t\x12\x13\n\x0b\x61rrivedTime\x18\x04 \x01(\x03\"?\n\x13UserMessageSchedule\x12\x11\n\tmessageId\x18\x01 \x01(\t\x12\x15\n\rscheduledTime\x18\x02 \x01(\x03\"\x96\x01\n\x0bUserMission\x12\x11\n\tmissionId\x18\x01 \x01(\t\x12\x18\n\x10\x63urrentThreshold\x18\x02 \x01(\x03\x12\x10\n\x08progress\x18\x03 \x01(\x03\x12\x30\n\nstatusType\x18\x04 \x01(\x0e\x32\x1c.ProtoEnum.MissionStatusType\x12\x16\n\x0elastUpdateTime\x18\x05 \x01(\x03\"\x1c\n\tUserMusic\x12\x0f\n\x07musicId\x18\x01 \x01(\t\"\xe1\x02\n\tUserPhoto\x12\x0f\n\x07photoId\x18\x01 \x01(\t\x12\x0f\n\x07\x61ssetId\x18\x02 \x01(\t\x12,\n\timageType\x18\x03 \x01(\x0e\x32\x19.ProtoEnum.PhotoImageType\x12\x14\n\x0c\x63haracterIds\x18\x04 \x03(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0e\n\x06rarity\x18\x06 \x01(\x05\x12\x11\n\tplaceName\x18\x07 \x01(\t\x12\x11\n\teventName\x18\x08 \x01(\t\x12\x0e\n\x06locked\x18\t \x01(\x08\x12\r\n\x05level\x18\n \x01(\x05\x12\x12\n\nrerollable\x18\x0b \x01(\x08\x12\x30\n\tabilities\x18\x0c \x03(\x0b\x32\x1d.transaction.UserPhotoAbility\x12\x14\n\x0cshootingTime\x18\r \x01(\x03\x12\x18\n\x10\x66ocusCharacterId\x18\x0e \x01(\t\x12\x15\n\rphotoRecipeId\x18\x0f \x01(\t\"v\n\x10UserPhotoAbility\x12\x16\n\x0ephotoAbilityId\x18\x01 \x01(\t\x12\x13\n\x0b\x65\x66\x66\x65\x63tValue\x18\x02 \x01(\x03\x12\x11\n\tmissionId\x18\x03 \x01(\t\x12\r\n\x05grade\x18\x04 \x01(\x05\x12\x13\n\x0bisAvailable\x18\x05 \x01(\x08\"8\n\x0fUserPhotoRecipe\x12\x15\n\rphotoRecipeId\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"\xed\x03\n\x0bUserProfile\x12\x16\n\x0e\x66\x61voriteCardId\x18\x01 \x01(\t\x12\x17\n\x0f\x66\x61voritePhotoId\x18\x02 \x01(\t\x12\x1c\n\x14\x66\x61voriteCharacterIds\x18\x03 \x03(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12\x12\n\nbirthMonth\x18\x05 \x01(\x03\x12\x10\n\x08\x62irthDay\x18\x06 \x01(\x03\x12\x38\n\x0e\x62\x61\x63kgroundType\x18\x07 \x01(\x0e\x32 .ProtoEnum.ProfileBackgroundType\x12\x30\n\nlayoutType\x18\x08 \x01(\x0e\x32\x1c.ProtoEnum.ProfileLayoutType\x12-\n\x0btwitterInfo\x18\t \x01(\x0b\x32\x18.transaction.TwitterInfo\x12\x14\n\x0c\x64\x65\x63orationId\x18\n \x01(\t\x12:\n\x0finformationType\x18\x0b \x01(\x0e\x32!.ProtoEnum.ProfileInformationType\x12.\n\tcolorType\x18\x0c \x01(\x0e\x32\x1b.ProtoEnum.ProfileColorType\x12;\n\x17\x66\x61voriteCardDisplayType\x18\r \x01(\x0e\x32\x1a.ProtoEnum.CardDisplayType\"\xd7\x02\n\tUserQuest\x12\x0f\n\x07questId\x18\x01 \x01(\t\x12\x17\n\x0f\x64\x61ilyClearCount\x18\x02 \x01(\x05\x12\x17\n\x0flastClearedTime\x18\x03 \x01(\x03\x12\x14\n\x0chighestScore\x18\x04 \x01(\x03\x12\x18\n\x10highestScoreTime\x18\x05 \x01(\x03\x12\x13\n\x0bhighestRank\x18\x06 \x01(\x03\x12\"\n\x1a\x63urrentRankingHighestScore\x18\x07 \x01(\x03\x12&\n\x1e\x63urrentRankingHighestScoreTime\x18\x08 \x01(\x03\x12!\n\x19\x63urrentRankingHighestRank\x18\t \x01(\x03\x12\x1e\n\x16\x63urrentRankingSeasonID\x18\n \x01(\t\x12\x33\n\x10highestScoreRank\x18\x64 \x01(\x0e\x32\x19.ProtoEnum.ResultRankType\"_\n\tUserStory\x12\x0f\n\x07storyId\x18\x01 \x01(\t\x12.\n\nstatusType\x18\x02 \x01(\x0e\x32\x1a.ProtoEnum.StoryStatusType\x12\x11\n\tisInvalid\x18\x03 \x01(\x08\"\x8e\x01\n\rUserTelephone\x12\x13\n\x0btelephoneId\x18\x01 \x01(\t\x12\x14\n\x0cunlockedTime\x18\x02 \x01(\x03\x12\x15\n\rscheduledTime\x18\x03 \x01(\x03\x12;\n\x13telephoneStatusType\x18\x04 \x01(\x0e\x32\x1e.ProtoEnum.TelephoneStatusType\"\x91\x01\n\x11\x43onsumptionResult\x12-\n\x0cresourceType\x18\x01 \x01(\x0e\x32\x17.ProtoEnum.ResourceType\x12\x12\n\nresourceId\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\x12\x14\n\x0c\x62\x65\x66oreAmount\x18\x04 \x01(\x03\x12\x13\n\x0b\x61\x66terAmount\x18\x05 \x01(\x03\"P\n\tMasterTag\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x32\n\x0emasterTagPacks\x18\x02 \x03(\x0b\x32\x1a.transaction.MasterTagPack\"i\n\rMasterTagPack\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x12\x10\n\x08\x66ileSize\x18\x03 \x01(\x05\x12\x11\n\tcryptoKey\x18\x04 \x01(\t\x12\x13\n\x0b\x64ownloadUrl\x18\x05 \x01(\t\"[\n\x06Reward\x12-\n\x0cresourceType\x18\x01 \x01(\x0e\x32\x17.ProtoEnum.ResourceType\x12\x12\n\nresourceId\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x03\"\xa8\x02\n\x0cRewardResult\x12-\n\x0cresourceType\x18\x01 \x01(\x0e\x32\x17.ProtoEnum.ResourceType\x12\x12\n\nresourceId\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\x12\x14\n\x0c\x62\x65\x66oreAmount\x18\x04 \x01(\x03\x12\x13\n\x0b\x61\x66terAmount\x18\x05 \x01(\x03\x12\r\n\x05isNew\x18\x06 \x01(\x08\x12\x12\n\nisTruncate\x18\x07 \x01(\x08\x12\x0e\n\x06isGift\x18\x08 \x01(\x08\x12\x39\n\x16\x64uplicateRewardResults\x18\t \x03(\x0b\x32\x19.transaction.RewardResult\x12,\n\x0f\x61\x64\x64itionalGifts\x18\n \x03(\x0b\x32\x13.transaction.Reward\"o\n\x1cUserActivityFanEventProgress\x12\x34\n\x11\x62\x65stScoreRankType\x18\x01 \x01(\x0e\x32\x19.ProtoEnum.ResultRankType\x12\x19\n\x11\x62\x65stScoreRankPlus\x18\x02 \x01(\x03\"7\n\x0bUserBalance\x12\x13\n\x0b\x66reeBalance\x18\x01 \x01(\x05\x12\x13\n\x0bpaidBalance\x18\x02 \x01(\x05\"&\n\tUserBuddy\x12\x19\n\x11\x64\x61ilyRentalAmount\x18\x01 \x01(\x03\"H\n\x0fUserCardSupport\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0e\n\x06\x63\x61rdId\x18\x02 \x01(\t\x12\x15\n\rremovableTime\x18\x04 \x01(\x03\"(\n\x08UserDeck\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xad\x01\n\x10UserDeckPosition\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x10\n\x08position\x18\x02 \x01(\x05\x12\x0e\n\x06\x63\x61rdId\x18\x03 \x01(\t\x12\x18\n\x10part1AccessoryId\x18\x04 \x01(\t\x12\x18\n\x10part2AccessoryId\x18\x05 \x01(\t\x12\x10\n\x08photoIds\x18\x06 \x03(\t\x12\x11\n\tcostumeId\x18\x07 \x01(\t\x12\x0e\n\x06hairId\x18\x08 \x01(\t\"b\n\x0fUserGachaButton\x12\x15\n\rgachaButtonId\x18\x01 \x01(\t\x12\x10\n\x08\x64rawTime\x18\x02 \x01(\x03\x12\x12\n\ntodayCount\x18\x03 \x01(\x05\x12\x12\n\ntotalCount\x18\x04 \x01(\x05\"\xd0\x01\n\x08UserGift\x12\x0e\n\x06giftId\x18\x01 \x01(\t\x12-\n\x0cresourceType\x18\x02 \x01(\x0e\x32\x17.ProtoEnum.ResourceType\x12\x12\n\nresourceId\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x12\n\npostedTime\x18\x06 \x01(\x03\x12\x11\n\tlimitTime\x18\x07 \x01(\x03\x12)\n\tphotoGift\x18\x08 \x01(\x0b\x32\x16.transaction.PhotoGift\"\x19\n\tPhotoGift\x12\x0c\n\x04name\x18\x01 \x01(\t\"\xe1\x01\n\x0fUserGiftHistory\x12\x0e\n\x06giftId\x18\x01 \x01(\t\x12-\n\x0cresourceType\x18\x02 \x01(\x0e\x32\x17.ProtoEnum.ResourceType\x12\x12\n\nresourceId\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x03\x12\x0f\n\x07message\x18\x05 \x01(\t\x12\x12\n\npostedTime\x18\x06 \x01(\x03\x12\x14\n\x0creceivedTime\x18\x07 \x01(\x03\x12\x30\n\tphotoGift\x18\x08 \x01(\x0b\x32\x1d.transaction.PhotoGiftHistory\" \n\x10PhotoGiftHistory\x12\x0c\n\x04name\x18\x01 \x01(\t\"G\n\nUserInvite\x12\x12\n\ninviteCode\x18\x01 \x01(\t\x12%\n\x1dreceivedHostRewardTotalAmount\x18\x02 \x01(\x03\"k\n\x10UserNotification\x12\x35\n\x10notificationType\x18\x01 \x01(\x0e\x32\x1b.ProtoEnum.NotificationType\x12\r\n\x05valid\x18\x02 \x01(\x08\x12\x11\n\tstartTime\x18\x03 \x01(\x03\"K\n\x0fUserPhotoReport\x12&\n\x06photos\x18\x01 \x03(\x0b\x32\x16.transaction.UserPhoto\x12\x10\n\x08received\x18\x02 \x01(\x08\"D\n\tUserPoint\x12\'\n\tpointType\x18\x01 \x01(\x0e\x32\x14.ProtoEnum.PointType\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\"?\n\x0bTwitterInfo\x12\x15\n\rtwitterUserID\x18\x01 \x01(\t\x12\x19\n\x11twitterScreenName\x18\x02 \x01(\t\"8\n\nUserPublic\x12\x14\n\x0cserverUserId\x18\x01 \x01(\t\x12\x14\n\x0cpublicUserId\x18\x02 \x01(\t\"K\n\tUserStaff\x12/\n\rparameterType\x18\x01 \x01(\x0e\x32\x18.ProtoEnum.ParameterType\x12\r\n\x05level\x18\x02 \x01(\x05\"\xd8\x02\n\x0eUserTotalCount\x12\x12\n\nloginCount\x18\x01 \x01(\x03\x12\x1b\n\x13marketExchangeCount\x18\x03 \x01(\x03\x12\x17\n\x0fphotoShootCount\x18\x04 \x01(\x03\x12\x17\n\x0fstaffTrainCount\x18\x05 \x01(\x03\x12\x17\n\x0fpointGoldAmount\x18\x06 \x01(\x03\x12\x16\n\x0e\x66orumLikeCount\x18\x07 \x01(\x03\x12\x1d\n\x15\x66orumCreateReplyCount\x18\x08 \x01(\x03\x12\x1d\n\x15\x61\x63tivityFanEventCount\x18\t \x01(\x03\x12 \n\x18\x61\x63tivityPromotionMinutes\x18\n \x01(\x03\x12\x1c\n\x14\x61\x63tivityRefreshCount\x18\x0b \x01(\x03\x12\x19\n\x11guildCheckInCount\x18\x0c \x01(\x03\x12\x19\n\x11photoRetouchCount\x18\r \x01(\x03\"K\n\x0cUserTutorial\x12-\n\x0ctutorialType\x18\x01 \x01(\x0e\x32\x17.ProtoEnum.TutorialType\x12\x0c\n\x04step\x18\x02 \x01(\x03\x42>Z\x1bsolis/pkg/proto/transaction\xaa\x02\x1eSolis.Common.Proto.Transactionb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ProtoTransaction_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\033solis/pkg/proto/transaction\252\002\036Solis.Common.Proto.Transaction'
  _PAYSLIP._serialized_start=57
  _PAYSLIP._serialized_end=643
  _USER._serialized_start=646
  _USER._serialized_end=1345
  _USERACCESSORY._serialized_start=1347
  _USERACCESSORY._serialized_end=1399
  _USERAREA._serialized_start=1401
  _USERAREA._serialized_end=1502
  _USERCARD._serialized_start=1505
  _USERCARD._serialized_end=2502
  _USERCHARACTER._serialized_start=2505
  _USERCHARACTER._serialized_end=2939
  _USERCHARACTERMUSIC._serialized_start=2941
  _USERCHARACTERMUSIC._serialized_end=3043
  _USERCOSTUME._serialized_start=3045
  _USERCOSTUME._serialized_end=3116
  _USERDECORATION._serialized_start=3118
  _USERDECORATION._serialized_end=3156
  _USEREMBLEM._serialized_start=3158
  _USEREMBLEM._serialized_end=3188
  _USERHAIR._serialized_start=3190
  _USERHAIR._serialized_end=3233
  _USERHIERARCHY._serialized_start=3236
  _USERHIERARCHY._serialized_end=3457
  _USERHOMEPOSITION._serialized_start=3460
  _USERHOMEPOSITION._serialized_end=3606
  _USERHOMETALK._serialized_start=3608
  _USERHOMETALK._serialized_end=3642
  _USERITEM._serialized_start=3644
  _USERITEM._serialized_end=3707
  _USERLOGINBONUS._serialized_start=3710
  _USERLOGINBONUS._serialized_end=3839
  _USERMESSAGE._serialized_start=3842
  _USERMESSAGE._serialized_end=3984
  _USERMESSAGESCHEDULE._serialized_start=3986
  _USERMESSAGESCHEDULE._serialized_end=4049
  _USERMISSION._serialized_start=4052
  _USERMISSION._serialized_end=4202
  _USERMUSIC._serialized_start=4204
  _USERMUSIC._serialized_end=4232
  _USERPHOTO._serialized_start=4235
  _USERPHOTO._serialized_end=4588
  _USERPHOTOABILITY._serialized_start=4590
  _USERPHOTOABILITY._serialized_end=4708
  _USERPHOTORECIPE._serialized_start=4710
  _USERPHOTORECIPE._serialized_end=4766
  _USERPROFILE._serialized_start=4769
  _USERPROFILE._serialized_end=5262
  _USERQUEST._serialized_start=5265
  _USERQUEST._serialized_end=5608
  _USERSTORY._serialized_start=5610
  _USERSTORY._serialized_end=5705
  _USERTELEPHONE._serialized_start=5708
  _USERTELEPHONE._serialized_end=5850
  _CONSUMPTIONRESULT._serialized_start=5853
  _CONSUMPTIONRESULT._serialized_end=5998
  _MASTERTAG._serialized_start=6000
  _MASTERTAG._serialized_end=6080
  _MASTERTAGPACK._serialized_start=6082
  _MASTERTAGPACK._serialized_end=6187
  _REWARD._serialized_start=6189
  _REWARD._serialized_end=6280
  _REWARDRESULT._serialized_start=6283
  _REWARDRESULT._serialized_end=6579
  _USERACTIVITYFANEVENTPROGRESS._serialized_start=6581
  _USERACTIVITYFANEVENTPROGRESS._serialized_end=6692
  _USERBALANCE._serialized_start=6694
  _USERBALANCE._serialized_end=6749
  _USERBUDDY._serialized_start=6751
  _USERBUDDY._serialized_end=6789
  _USERCARDSUPPORT._serialized_start=6791
  _USERCARDSUPPORT._serialized_end=6863
  _USERDECK._serialized_start=6865
  _USERDECK._serialized_end=6905
  _USERDECKPOSITION._serialized_start=6908
  _USERDECKPOSITION._serialized_end=7081
  _USERGACHABUTTON._serialized_start=7083
  _USERGACHABUTTON._serialized_end=7181
  _USERGIFT._serialized_start=7184
  _USERGIFT._serialized_end=7392
  _PHOTOGIFT._serialized_start=7394
  _PHOTOGIFT._serialized_end=7419
  _USERGIFTHISTORY._serialized_start=7422
  _USERGIFTHISTORY._serialized_end=7647
  _PHOTOGIFTHISTORY._serialized_start=7649
  _PHOTOGIFTHISTORY._serialized_end=7681
  _USERINVITE._serialized_start=7683
  _USERINVITE._serialized_end=7754
  _USERNOTIFICATION._serialized_start=7756
  _USERNOTIFICATION._serialized_end=7863
  _USERPHOTOREPORT._serialized_start=7865
  _USERPHOTOREPORT._serialized_end=7940
  _USERPOINT._serialized_start=7942
  _USERPOINT._serialized_end=8010
  _TWITTERINFO._serialized_start=8012
  _TWITTERINFO._serialized_end=8075
  _USERPUBLIC._serialized_start=8077
  _USERPUBLIC._serialized_end=8133
  _USERSTAFF._serialized_start=8135
  _USERSTAFF._serialized_end=8210
  _USERTOTALCOUNT._serialized_start=8213
  _USERTOTALCOUNT._serialized_end=8557
  _USERTUTORIAL._serialized_start=8559
  _USERTUTORIAL._serialized_end=8634
# @@protoc_insertion_point(module_scope)
