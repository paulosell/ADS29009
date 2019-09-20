#include <netdb.h> 
#include <netinet/in.h> 
#include <stdlib.h> 
#include <stdio.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h> 
#define MAX 15 
#define PORT 65432 
#define SA struct sockaddr 

// Function designed for chat between client and server. 
void func(int sockfd){
	char buff[MAX]; 
	int n; 
	// infinite loop for chat 
	for (;;) { 
		bzero(buff, MAX); 
		n = 0;
		// read the message from client and copy it in buffer 
		read(sockfd, buff, sizeof(buff)); 
		if 		(strncmp("F", buff, 1) == 0) n = 1; 		//frente	
		else if (strncmp("R", buff, 1) == 0) n = 2;			//tras
		else if (strncmp("E", buff, 1) == 0) n = 3;			//esquerda
		else if (strncmp("D", buff, 1) == 0) n = 4;			//direita
		else if (strncmp("exit", buff, 4) == 0) n = 5;		//encerrar
		//n = atoi(buff);
		//printf("%d\n", n);
		switch(n){
			case 1:
				//.........
				bzero(buff, MAX); 
				strcpy(buff, "Frente ok");
				write(sockfd, buff, sizeof(buff)); 
				break;
			case 2:
				//.........
				bzero(buff, MAX); 
				strcpy(buff, "Tras ok");
				write(sockfd, buff, sizeof(buff)); 
				break;
			case 3:
				//.........
				bzero(buff, MAX); 
				strcpy(buff, "Esquerda ok");
				write(sockfd, buff, sizeof(buff)); 
				break;
			case 4:
				//.........
				bzero(buff, MAX); 
				strcpy(buff, "Direita ok");
				write(sockfd, buff, sizeof(buff)); 
				break;
			case 5:
				strcpy(buff, "exit"); 
				write(sockfd, buff, sizeof(buff));
				strcpy(buff, "exit");
				break;
			default:
				bzero(buff, MAX);
				strcpy(buff, "nok"); 
				write(sockfd, buff, sizeof(buff));
				break;
		}
		if (strncmp("exit", buff, 4) == 0) { 
			printf("Server Exit..."); 
			break; 
		} 
	} 
} 

// Driver function 
int main() 
{ 
	int sockfd, connfd, len; 
	struct sockaddr_in servaddr, cli; 

	// socket create and verification 
	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
	if (sockfd == -1) { 
		printf("socket creation failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully created..\n"); 
	bzero(&servaddr, sizeof(servaddr)); 

	// assign IP, PORT 
	servaddr.sin_family = AF_INET; 
	servaddr.sin_addr.s_addr = htonl(INADDR_ANY); 
	servaddr.sin_port = htons(PORT); 

	// Binding newly created socket to given IP and verification 
	if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) { 
		printf("socket bind failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully binded..\n"); 

	// Now server is ready to listen and verification 
	if ((listen(sockfd, 5)) != 0) { 
		printf("Listen failed...\n"); 
		exit(0); 
	} 
	else
		printf("Server listening..\n"); 
	len = sizeof(cli); 

	// Accept the data packet from client and verification 
	connfd = accept(sockfd, (SA*)&cli, &len); 
	if (connfd < 0) { 
		printf("server acccept failed...\n"); 
		exit(0); 
	} 
	else
		printf("server acccept the client...\n"); 

	// Function for chatting between client and server 
	func(connfd); 

	// After chatting close the socket 
	close(sockfd); 
} 

