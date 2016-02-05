#include "state.h"
#include <stdlib.h>
#include <inttypes.h>
#define MAX_M_RUN  10
#define VERIFIER   3289
//caution. No error checking for malloc. 
//It is assumed that malloc always succeeds. So it is not a reliable library.

int checker=0;

CHANDLE state_machiner_init(){

    //set up local data structure.
    //initialize a table state machines
    if(checker != 0)
        return((CHANDLE)(intptr_t) checker); // if client calls the init() more than once by mistake,
    //then just ignore multiple calls and act on first call only.


    HSTRUCT** memtable = malloc((MAX_M_RUN+1)*sizeof(void*));
    //make sure table is initialized to 0
    checker = (intptr_t)memtable; //set up a checker varialbe to verify that 
     //whatever client will send to other functions
    //to make sure that only valid pointers are derefrenced.
    
    int j=0;
    for(j=0; j<=MAX_M_RUN; j++)
        memtable[j]=NULL;

    HSTRUCT *hsp= malloc(sizeof(HSTRUCT)); // allocate memory for first structure
    hsp->count=0;
    hsp->data= (void *)(intptr_t) VERIFIER;
    
    memtable[0] = hsp;
    return(memtable);
}

MHANDLE build_machine(CHANDLE chandle, FILE *fd){

    HSTRUCT *hsp0, *hsp1;
    int j=1;
    int machines_running=0;
    if(chandle == NULL)
        return(-300); //-300: Error:Expected a CHANDLE* but got NULL.

    if( checker != ((intptr_t) chandle))
        return(-400); // -400: Error: client passed an invalid pointer.
         
    if(chandle[0] -> data != (int *) VERIFIER)
        return(-401); //-401: Error: Verification of pointer failed.
    hsp0 = chandle[0];
    // Find the number of machines currently running
    machines_running = hsp0 -> count;
    if(machines_running >= MAX_M_RUN) 
        return(-100); // -100 = Error: Cannot manage more than (MAX_M_RUN -1) machines
    hsp0 -> count += 1;
    //allocate memory for the management data for new machine.
    hsp1 = malloc(sizeof(HSTRUCT));
    void *m_state =malloc(sizeof(int)); 
    hsp1 -> data = m_state; 
    
    //locate an empty space in the CHANDLE array and put hsp1 there.
    while(chandle[j] != NULL){
        j++;
        if(j > MAX_M_RUN)
            return(-200); //-200: Error: Could not find an empty space for new
        //machine. Possibly the internal data structure has become corrupt.
    }
    chandle[j] = hsp1; //all is well. put the address in table and return its handle.

    return(j);
}

int state_machiner_close(CHANDLE chandle){
    //Safely shuts downs the machines manager.
    //Deallocate memory.
    if(checker == 0)
        return(-500); 
    //-500 : Error: Trying to close a non-existing machiner.
    if(chandle == NULL) 
        return(-300);
    //-300: Error: Trying to close() on NULL.
    if( checker != ((intptr_t) chandle))
        return(-400); // -400: Error: Trying to close() on invalid handle.
         
    if(chandle[0] -> data != (int *) VERIFIER)
        return(-401); //-401: Error: Verification of pointer failed.

    int j=1; // Do not start j with j=0. It will cause a segmentation fault.
    for(j=1; j<= MAX_M_RUN; j++){
        if (chandle[j] !=NULL){
            if((chandle[j] -> data) != NULL)
                free(chandle[j] -> data);
            free(chandle[j]);
        }
    }
   //memory allocated by machines is freed.
   //Finally free memtable
   free(chandle);
   checker=0;
   return(0); 
}
