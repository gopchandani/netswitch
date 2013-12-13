

// This C++ file was created by SanEditor

#include "Atomic/one_controller_one_aggregator/one_controller_one_aggregatorSAN.h"

#include <stdlib.h>
#include <iostream>

#include <math.h>


/*****************************************************************
                         one_controller_one_aggregatorSAN Constructor             
******************************************************************/


one_controller_one_aggregatorSAN::one_controller_one_aggregatorSAN(){


  Activity* InitialActionList[2]={
    &Controller_UpdateProcessing, //0
    &UpdateArrival  // 1
  };

  BaseGroupClass* InitialGroupList[2]={
    (BaseGroupClass*) &(Controller_UpdateProcessing), 
    (BaseGroupClass*) &(UpdateArrival)
  };

  Controller_NumberOfTokens = new Place("Controller_NumberOfTokens" ,0);
  BaseStateVariableClass* InitialPlaces[1]={
    Controller_NumberOfTokens   // 0
  };
  BaseStateVariableClass* InitialROPlaces[0]={
  };
  initializeSANModelNow("one_controller_one_aggregator", 1, InitialPlaces, 
                        0, InitialROPlaces, 
                        2, InitialActionList, 2, InitialGroupList);


  assignPlacesToActivitiesInst();
  assignPlacesToActivitiesTimed();

  int AffectArcs[2][2]={ 
    {0,0}, {0,1}
  };
  for(int n=0;n<2;n++) {
    AddAffectArc(InitialPlaces[AffectArcs[n][0]],
                 InitialActionList[AffectArcs[n][1]]);
  }
  int EnableArcs[1][2]={ 
    {0,0}
  };
  for(int n=0;n<1;n++) {
    AddEnableArc(InitialPlaces[EnableArcs[n][0]],
                 InitialActionList[EnableArcs[n][1]]);
  }

  for(int n=0;n<2;n++) {
    InitialActionList[n]->LinkVariables();
  }
  CustomInitialization();

}

void one_controller_one_aggregatorSAN::CustomInitialization() {

}
one_controller_one_aggregatorSAN::~one_controller_one_aggregatorSAN(){
  for (int i = 0; i < NumStateVariables-NumReadOnlyPlaces; i++)
    delete LocalStateVariables[i];
};

void one_controller_one_aggregatorSAN::assignPlacesToActivitiesInst(){
}
void one_controller_one_aggregatorSAN::assignPlacesToActivitiesTimed(){
  Controller_UpdateProcessing.Controller_NumberOfTokens = (Place*) LocalStateVariables[0];
  UpdateArrival.Controller_NumberOfTokens = (Place*) LocalStateVariables[0];
}
/*****************************************************************/
/*                  Activity Method Definitions                  */
/*****************************************************************/

/*======================Controller_UpdateProcessingActivity========================*/

one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::Controller_UpdateProcessingActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("Controller_UpdateProcessing",0,Exponential, RaceEnabled, 1,1, false);
}

one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::~Controller_UpdateProcessingActivity(){
  delete[] TheDistributionParameters;
}

void one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::LinkVariables(){
  Controller_NumberOfTokens->Register(&Controller_NumberOfTokens_Mobius_Mark);
}

bool one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=((PickupUpdateForProcessingIP()));
  return NewEnabled;
}

    bool one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::PickupUpdateForProcessingIP(){
if (Controller_NumberOfTokens->Mark() > 0)
{
  return 1;
} else
{
  return 0;
}


return 0;
    }

double one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::Rate(){
  return 20.0;
  return 1.0;  // default rate if none is specified
}

double one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::Weight(){ 
  return 1;
}

bool one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::ReactivationPredicate(){ 
  return false;
}

bool one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::ReactivationFunction(){ 
  return false;
}

double one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::SampleDistribution(){
  return TheDistribution->Exponential(20.0);
}

double* one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::Rank(){
  return 1;
}

BaseActionClass* one_controller_one_aggregatorSAN::Controller_UpdateProcessingActivity::Fire(){
  Controller_NumberOfTokens->Mark() -- ;
  return this;
}

/*======================UpdateArrivalActivity========================*/

one_controller_one_aggregatorSAN::UpdateArrivalActivity::UpdateArrivalActivity(){
  TheDistributionParameters = new double[1];
  ActivityInitialize("UpdateArrival",1,Exponential, RaceEnabled, 1,0, false);
}

one_controller_one_aggregatorSAN::UpdateArrivalActivity::~UpdateArrivalActivity(){
  delete[] TheDistributionParameters;
}

void one_controller_one_aggregatorSAN::UpdateArrivalActivity::LinkVariables(){
  Controller_NumberOfTokens->Register(&Controller_NumberOfTokens_Mobius_Mark);
}

bool one_controller_one_aggregatorSAN::UpdateArrivalActivity::Enabled(){
  OldEnabled=NewEnabled;
  NewEnabled=(true);
  return NewEnabled;
}

double one_controller_one_aggregatorSAN::UpdateArrivalActivity::Rate(){
  return 10.0;
  return 1.0;  // default rate if none is specified
}

double one_controller_one_aggregatorSAN::UpdateArrivalActivity::Weight(){ 
  return 1;
}

bool one_controller_one_aggregatorSAN::UpdateArrivalActivity::ReactivationPredicate(){ 
  return false;
}

bool one_controller_one_aggregatorSAN::UpdateArrivalActivity::ReactivationFunction(){ 
  return false;
}

double one_controller_one_aggregatorSAN::UpdateArrivalActivity::SampleDistribution(){
  return TheDistribution->Exponential(10.0);
}

double* one_controller_one_aggregatorSAN::UpdateArrivalActivity::ReturnDistributionParameters(){
  TheDistributionParameters[0] = Rate();
  return TheDistributionParameters;
}

int one_controller_one_aggregatorSAN::UpdateArrivalActivity::Rank(){
  return 1;
}

BaseActionClass* one_controller_one_aggregatorSAN::UpdateArrivalActivity::Fire(){
  if (Controller_NumberOfTokens->Mark() < 10)
{
  Controller_NumberOfTokens->Mark()++;
}

  return this;
}

