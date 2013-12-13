#include "arewardPVNodes.h"

arewardPV0Worker::arewardPV0Worker()
{
  NumModels = 1;
  TheModelPtr = new BaseModelClass**[NumModels];
  TheModelPtr[0] = (BaseModelClass**)(&one_controller_one_aggregator);
}

arewardPV0Worker::~arewardPV0Worker() {
  delete [] TheModelPtr;
}

double arewardPV0Worker::Reward_Function(void) {

return one_controller_one_aggregator->Controller_NumberOfTokens->Mark();

return (0);



}

arewardPV0::arewardPV0(int timeindex) {
  TheModelPtr = (BaseModelClass**)(&Theone_controller_one_aggregatorSAN);
  double startpts[1]={10000.0};
  double stoppts[1]={10000.0};
  Initialize("areward",(RewardType)0,1, startpts, stoppts, timeindex, 0,1, 1);
  AddVariableDependency("Controller_NumberOfTokens","one_controller_one_aggregator");
}

arewardPV0::~arewardPV0() {
  for(int i = 0; i < NumberOfWorkers; i++) {
    delete[] WorkerList[i]->Name;
    delete WorkerList[i];
  }
}

void arewardPV0::CreateWorkerList(void) {
  for(int i = 0; i < NumberOfWorkers; i++)
    WorkerList[i] = new arewardPV0Worker;
}
arewardPV1Worker::arewardPV1Worker()
{
  NumModels = 1;
  TheModelPtr = new BaseModelClass**[NumModels];
  TheModelPtr[0] = (BaseModelClass**)(&one_controller_one_aggregator);
}

arewardPV1Worker::~arewardPV1Worker() {
  delete [] TheModelPtr;
}

double arewardPV1Worker::Reward_Function(void) {

return one_controller_one_aggregator->Controller_NumberOfTokens->Mark();

return (0);



}

arewardPV1::arewardPV1(int timeindex) {
  TheModelPtr = (BaseModelClass**)(&Theone_controller_one_aggregatorSAN);
  double startpts[1]={0.0};
  double stoppts[1]={0.0+1.0};
  Initialize("assreward",(RewardType)3,1, startpts, stoppts, timeindex, 0,1, 1);
  Type = steady_state;
  AddVariableDependency("Controller_NumberOfTokens","one_controller_one_aggregator");
}

arewardPV1::~arewardPV1() {
  for(int i = 0; i < NumberOfWorkers; i++) {
    delete[] WorkerList[i]->Name;
    delete WorkerList[i];
  }
}

void arewardPV1::CreateWorkerList(void) {
  for(int i = 0; i < NumberOfWorkers; i++)
    WorkerList[i] = new arewardPV1Worker;
}
