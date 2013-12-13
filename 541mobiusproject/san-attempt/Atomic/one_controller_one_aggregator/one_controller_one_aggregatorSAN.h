#ifndef one_controller_one_aggregatorSAN_H_
#define one_controller_one_aggregatorSAN_H_

#include "Cpp/BaseClasses/EmptyGroup.h"
#include "Cpp/BaseClasses/PreselectGroup.h"
#include "Cpp/BaseClasses/PostselectGroup.h"
#include "Cpp/BaseClasses/state/StructStateVariable.h"
#include "Cpp/BaseClasses/state/ArrayStateVariable.h"
#include "Cpp/BaseClasses/SAN/SANModel.h" 
#include "Cpp/BaseClasses/SAN/Place.h"
#include "Cpp/BaseClasses/SAN/ExtendedPlace.h"
extern UserDistributions* TheDistribution;

void MemoryError();


/*********************************************************************
               one_controller_one_aggregatorSAN Submodel Definition                   
*********************************************************************/

class one_controller_one_aggregatorSAN:public SANModel{
public:

class Controller_UpdateProcessingActivity:public Activity {
public:

  Place* Controller_NumberOfTokens;
  short* Controller_NumberOfTokens_Mobius_Mark;

  double* TheDistributionParameters;
  Controller_UpdateProcessingActivity();
  ~Controller_UpdateProcessingActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
 bool PickupUpdateForProcessingIP();
}; // Controller_UpdateProcessingActivityActivity

class UpdateArrivalActivity:public Activity {
public:

  Place* Controller_NumberOfTokens;
  short* Controller_NumberOfTokens_Mobius_Mark;

  double* TheDistributionParameters;
  UpdateArrivalActivity();
  ~UpdateArrivalActivity();
  bool Enabled();
  void LinkVariables();
  double Weight();
  bool ReactivationPredicate();
  bool ReactivationFunction();
  double SampleDistribution();
  double* ReturnDistributionParameters();
  int Rank();
  BaseActionClass* Fire();
  double Rate();
}; // UpdateArrivalActivityActivity

  //List of user-specified place names
  Place* Controller_NumberOfTokens;

  // Create instances of all actvities
  Controller_UpdateProcessingActivity Controller_UpdateProcessing;
  UpdateArrivalActivity UpdateArrival;
  //Create instances of all groups 
  EmptyGroup ImmediateGroup;

  one_controller_one_aggregatorSAN();
  ~one_controller_one_aggregatorSAN();
  void CustomInitialization();

  void assignPlacesToActivitiesInst();
  void assignPlacesToActivitiesTimed();
}; // end one_controller_one_aggregatorSAN

#endif // one_controller_one_aggregatorSAN_H_
