#include "arewardPVModel.h"

arewardPVModel::arewardPVModel(bool expandTimeArrays) {
  TheModel=new one_controller_one_aggregatorSAN();
  DefineName("arewardPVModel");
  CreatePVList(2, expandTimeArrays);
  Initialize();
}



PerformanceVariableNode* arewardPVModel::createPVNode(int pvindex, int timeindex) {
  switch(pvindex) {
  case 0:
    return new arewardPV0(timeindex);
    break;
  case 1:
    return new arewardPV1(timeindex);
    break;
  }
  return NULL;
}
