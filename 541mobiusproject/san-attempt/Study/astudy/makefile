OBJS=astudyRangeStudy.o 


#include common Makefile for default targets
include ../../Makefile.project
include $(MOBIUSROOT)/Cpp/BaseClasses/Makefile.common

all: normal
opt: $(ROOTDIR)/lib/$(PLATFORM)/libastudyRangeStudy.a
normal debug trace: $(ROOTDIR)/lib/$(PLATFORM)/libastudyRangeStudy_debug.a

$(ROOTDIR)/lib/$(PLATFORM)/libastudyRangeStudy.a: FORCE
	$(MAKE) lib TARGET=libastudyRangeStudy.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="" ROOTLIBDIR="."

$(ROOTDIR)/lib/$(PLATFORM)/libastudyRangeStudy_debug.a: FORCE
	$(MAKE) lib TARGET=libastudyRangeStudy_debug.a OBJS="$(OBJS)" USERINCLUDE="$(USERINCLUDE)" TYPE="_debug" ROOTLIBDIR="."

clean_sub_dirs:

