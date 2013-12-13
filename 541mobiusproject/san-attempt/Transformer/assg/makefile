OBJS=


#include common Makefile for default targets
include ../../Makefile.project
include $(MOBIUSROOT)/Cpp/BaseClasses/Makefile.common

BINDIR=
MAINLIB=-lgenMain
MAINLIB_debug=-lgenMain_debug
SIMLIB=gen
SIMLIB_debug=gen_debug
SIMLIB_trace=gen_trace
PROJECTLIBS=-lastudyRangeStudy -larewardPV -lone_controller_one_aggregatorSAN 
PROJECTLIBS_debug=-lastudyRangeStudy_debug -larewardPV_debug -lone_controller_one_aggregatorSAN_debug 
MOBIUSLIBS=-lTRex -lStudy -lPV -lSAN -lbase -lstate -lmobutil -ldist 
MOBIUSLIBS_debug=-lTRex_debug -lStudy_debug -lPV_debug -lSAN_debug -lbase_debug -lstate_debug -lmobutil_debug -ldist_debug 
USERDEFLIBNAME=
USERDEFLIBDIR=

all: normal

opt \
assgGen_$(ARCH): SUBMODELS/opt
	$(MAKE) exec3 "TARGET=assgGen_$(ARCH)" "USERLIBDIR=-L$(MOBIUSROOT)/Cpp/lib/$(PLATFORM)$(FORCE_ARCH) $(USERDEFLIBDIR)" "USERLIB=$(MAINLIB) -l$(SIMLIB) $(USERDEFLIBNAME) $(PROJECTLIBS) $(USERDEFLIBNAME) $(MOBIUSLIBS)" 

normal debug \
assgGen_$(ARCH)_debug: SUBMODELS/debug
	$(MAKE) exec3 "TARGET=assgGen_$(ARCH)_debug" "USERLIBDIR=-L$(MOBIUSROOT)/Cpp/lib/$(PLATFORM)$(FORCE_ARCH) $(USERDEFLIBDIR)" "USERLIB=$(MAINLIB_debug) -l$(SIMLIB_debug) $(USERDEFLIBNAME) $(PROJECTLIBS_debug) $(USERDEFLIBNAME) $(MOBIUSLIBS_debug) " "BUILDTARGET=_debug"

trace \
assgGen_$(ARCH)_trace:
	$(MAKE) exec3 "TARGET=assgGen_$(ARCH)_trace" "USERLIBDIR=-L$(MOBIUSROOT)/Cpp/lib/$(PLATFORM)$(FORCE_ARCH) $(USERDEFLIBDIR)" "USERLIB=$(MAINLIB_debug) -l$(SIMLIB_trace) $(USERDEFLIBNAME) $(PROJECTLIBS_debug) $(USERDEFLIBNAME) $(MOBIUSLIBS_debug) " "BUILDTARGET=_debug"

clean_sub_dirs:
	cd ../../Atomic/one_controller_one_aggregator/ && $(MAKE) clean
	cd ../../Reward/areward/ && $(MAKE) clean
	cd ../../Study/astudy/ && $(MAKE) clean

SUBMODELS/opt SUBMODELS/debug:
	@echo "NEW_SUBMODEL_LIB:[one_controller_one_aggregator]"
	cd ../../Atomic/one_controller_one_aggregator/ && $(MAKE) $(@F)
	@echo "NEW_SUBMODEL_LIB:[areward]"
	cd ../../Reward/areward/ && $(MAKE) $(@F)
	@echo "NEW_SUBMODEL_LIB:[astudy]"
	cd ../../Study/astudy/ && $(MAKE) $(@F)


