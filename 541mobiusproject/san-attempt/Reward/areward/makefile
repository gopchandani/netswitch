OBJS=arewardPVNodes.o arewardPVModel.o 


#include common Makefile for default targets
include ../../Makefile.project
include $(MOBIUSROOT)/Cpp/BaseClasses/Makefile.common

all: normal
opt: $(ROOTDIR)/lib/$(PLATFORM)/libarewardPV.a
normal debug trace: $(ROOTDIR)/lib/$(PLATFORM)/libarewardPV_debug.a

$(ROOTDIR)/lib/$(PLATFORM)/libarewardPV.a: FORCE
	$(MAKE) lib TARGET=libarewardPV.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="" ROOTLIBDIR="."

$(ROOTDIR)/lib/$(PLATFORM)/libarewardPV_debug.a: FORCE
	$(MAKE) lib TARGET=libarewardPV_debug.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="_debug" ROOTLIBDIR="."

clean_sub_dirs:

