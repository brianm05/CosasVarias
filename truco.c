#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

#define CARTAS 3

struct cartaStruct{
    char carta[6];
    short num;
};

void sacarCarta(char c[6]){
    int palo,valor;

    valor=rand() % 10+1;  //genera un valor entre 0 y 9. se le agrega 1
    palo=rand() % 4;

    if(valor>0 && valor<=7){
        c[0]='0';
        c[1]=(char)valor+48;
    }else if(valor>=8 && valor<=10){
        c[0]='1';
        switch(valor){
            case 8:
                c[1]='0';
                break;
            case 9:
                c[1]='1';
                break;
            case 10:
                c[1]='2';
                break;
            default:
                break;
        }
    }
    c[2]='-';
    c[6]=' ';

    switch(palo){
        case 0:
            c[3]='E';
            c[4]='S';
            c[5]='P';
            break;
        case 1:
            c[3]='O';
            c[4]='R';
            c[5]='O';
            break;
        case 2:
            c[3]='C';
            c[4]='O';
            c[5]='P';
            break;
        case 3:
            c[3]='B';
            c[4]='A';
            c[5]='S';
            break;
        default:
            break;
    }
}

void repartirMano(struct cartaStruct cartasJugador[],struct cartaStruct cartasCPU[]){
    struct cartaStruct total[CARTAS*2];

    for(int j=0;j<CARTAS*2;j++){
        sacarCarta(total[j].carta);
        for(int k=0;k<CARTAS*2;k++){
            while( (strcmp(total[j].carta,total[k].carta) == 0) && (j!=k) ){
                sacarCarta(total[j].carta);
                k=0;
            }
        }
    }

    //los siguientes 2 for son para separar las cartas entre los dos jugadores.
    for(int i=0;i<CARTAS;i++){
        strcpy(cartasJugador[i].carta,total[i].carta);
    }
    for(int i=3,j=0;i<CARTAS*2;i++,j++){
        strcpy(cartasCPU[j].carta,total[i].carta);
    }

    //MOSTRAR TODAS LAS CARTAS
    /*
    for(int i=0;i<CARTAS*2;i++){
        printf("CARTA [%d]= %s\n",i,total[i].carta);
    }*/
}

void mostrarCartas(struct cartaStruct c[]){
    for(int i=0;i<CARTAS;i++){
        printf("%s| ",c[i].carta);
    }
    printf("\nCarta 1|Carta 2 |Carta 3 |");
}

void tirarCarta(struct cartaStruct c[]){
    int elec=-1,flag=0;
    do{
        printf("\nQue carta vas a tirar?");
        scanf("%d",&elec);
        switch(elec){
            case 1:
            case 2:
            case 3:
                flag=1;
                break;
            default:
                break;
        }
    }while(flag==0);
    printf("Seleccionaste la carta %d: %s.",elec,c[elec-1].carta);
}




int main(){
    srand(time(NULL));
    struct cartaStruct cartas[CARTAS];
    struct cartaStruct cartasCOM[CARTAS];


    repartirMano(cartas,cartasCOM);

    /*
    for(int i=0;i<CARTAS;i++){
        printf("CARTA JUGADOR[%d]= %s\n",i,cartas[i].carta);
    }
    for(int i=0;i<CARTAS;i++){
        printf("CARTA COM[%d]= %s\n",i,cartasCOM[i].carta);
    }*/

    printf("BIENVENIDO AL TRUCO.\n");
    mostrarCartas(cartas);
    tirarCarta(cartas);

return 0;}
