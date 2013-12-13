#ifndef _AREWARD_PVS_
#define _AREWARD_PVS_
#include <math.h>
#include "Cpp/Performance_Variables/PerformanceVariableNode.hpp"
#include "Atomic/one_controller_one_aggregator/one_controller_one_aggregatorSAN.h"
#include "Cpp/Performance_Variables/InstantOfTime.hpp"
#include "Cpp/Performance_Variables/SteadyState.hpp"


class arewardPV0Worker:public InstantOfTime
{
 public:
  one_controller_one_aggregatorSAN *one_controller_one_aggregator;
  
  arewardPV0Worker();
  ~arewardPV0Worker();
  double Reward_Function();
};

class arewardPV0:public PerformanceVariableNode
{
 public:
  one_controller_one_aggregatorSAN *Theone_controller_one_aggregatorSAN;

  arewardPV0Worker *arewardPV0WorkerList;

  arewardPV0(int timeindex=0);
  ~arewardPV0();
  void CreateWorkerList(void);
};

class arewardPV1Worker:public SteadyState
{
 public:
  one_controller_one_aggregatorSAN *one_controller_one_aggregator;
  
  arewardPV1Worker();
  ~arewardPV1Worker();
  double Reward_Function();
};

class arewardPV1:public PerformanceVariableNode
{
 public:
  one_controller_one_aggregatorSAN *Theone_controller_one_aggregatorSAN;

  arewardPV1Worker *arewardPV1WorkerList;

  arewardPV1(int timeindex=0);
  ~arewardPV1();
  void CreateWorkerList(void);
};

#endif
