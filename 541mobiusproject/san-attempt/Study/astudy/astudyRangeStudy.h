
#ifndef astudyRangeSTUDY_H_
#define astudyRangeSTUDY_H_

#include "Reward/areward/arewardPVNodes.h"
#include "Reward/areward/arewardPVModel.h"
#include "Cpp/Study/BaseStudyClass.hpp"


class astudyRangeStudy : public BaseStudyClass {
public:

astudyRangeStudy();
~astudyRangeStudy();

private:



void PrintGlobalValues(int);
void *GetGVValue(char *TheGVName);
void OverrideGVValue(char *TheGVName, void *TheGVValue);
void SetGVs(int expnum);
PVModel *GetPVModel(bool expandTimeArrays);
};

#endif

