#include <stdio.h>
#include "state.h"

int main(){
    FILE *fp;
    int j;

    CHANDLE chandle = state_machiner_init();
    printf("Tried to initialize the machiner. Got %d\n", (int)chandle);
    CHANDLE again = state_machiner_init();
    printf("Tried to initialize the machiner Again. Got %d\n", (int)again);
    for(j=1; j<=20; j++){
        MHANDLE mhandle = build_machine(chandle,fp);
        printf("Try number %d on build_machine(). Got %d\n", j,mhandle);
    }


    //The above calls were valid because a valid pointer was used by the client.
    //Now pass an invalid pointer
    MHANDLE w = build_machine((CHANDLE)34210, fp);
    printf("Tried build_machine() on invalid handle. Got %d\n", w);

    int validclose = state_machiner_close(chandle);
    printf("Tried close() on valid handle. Got %d\n", validclose);
    validclose = state_machiner_close(chandle);
    printf("Tried to close() a closed machiner. Got %d\n", validclose);
    validclose = state_machiner_close((CHANDLE) 3223);
    printf("Tried to close() on invalid handle.  Got %d\n", validclose);
  
    printf("No Segfaults: Program is terminating normally\n");
    return(0);
}
