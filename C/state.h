
#ifndef STATE_MACHINE_H
#define STATE_MACHINE_H
#include <stdio.h>

typedef struct handlestruct{
    int count;
    void *data;
}HSTRUCT;

typedef int MHANDLE;
typedef HSTRUCT** CHANDLE;

extern MHANDLE build_machine(CHANDLE, FILE *fd);
extern CHANDLE state_machiner_init();
extern int state_machiner_close(CHANDLE); 

#endif
