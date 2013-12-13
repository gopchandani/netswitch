OBJS=one_controller_one_aggregatorSAN.o 


#include common Makefile for default targets
include ../../Makefile.project
include $(MOBIUSROOT)/Cpp/BaseClasses/Makefile.common

all: normal
opt: $(ROOTDIR)/lib/$(PLATFORM)/libone_controller_one_aggregatorSAN.a
normal debug trace: $(ROOTDIR)/lib/$(PLATFORM)/libone_controller_one_aggregatorSAN_debug.a

$(ROOTDIR)/lib/$(PLATFORM)/libone_controller_one_aggregatorSAN.a: FORCE
	$(MAKE) lib TARGET=libone_controller_one_aggregatorSAN.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="" ROOTLIBDIR="."

$(ROOTDIR)/lib/$(PLATFORM)/libone_controller_one_aggregatorSAN_debug.a: FORCE
	$(MAKE) lib TARGET=libone_controller_one_aggregatorSAN_debug.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="_debug" ROOTLIBDIR="."

clean_sub_dirs:

