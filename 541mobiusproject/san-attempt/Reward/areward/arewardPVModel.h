#ifndef _AREWARD_PVMODEL_
#define _AREWARD_PVMODEL_
#include "arewardPVNodes.h"
#include "Cpp/Performance_Variables/PVModel.hpp"
#include "Atomic/one_controller_one_aggregator/one_controller_one_aggregatorSAN.h"
class arewardPVModel:public PVModel {
 protected:
  PerformanceVariableNode *createPVNode(int pvindex, int timeindex);
 public:
  arewardPVModel(bool expandtimepoints);
};

#endif
