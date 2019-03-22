B_8	EQU	7FFDH
C_8	EQU	7FFEH
CON_8	EQU	7FFFH

;--------------------------------------
	ORG	0000H
	LJMP	MAIN
	ORG	0200H
;--------------------------------------	
;	
MAIN:	
	MOV	A,#80H   ; 80H -> A
	MOV	DPTR,#CON_8
	MOVX	@DPTR,A
START:	
	MOV	A,#24H
	LCALL	CCC
	MOV	A,#90H
	LCALL	BBB  ; 跳转BBB
	LCALL	DE6S
LLL:	
	MOV	A,#0CH
	LCALL	CCC
	MOC	A,#30H
	LCALL	BBB
	LCALL	DE12S
	MOV	A,#04H
	LCALL	CCC
	MOV	A,#10H
	LCALL	BBB
	MOV	R2,#08H
TTT:	
	MOV	A,#14H
	LCALL	CCC
	MOV	A,#50H
	LCALL	BBB
	LCALL	DE02S
	MOV	A,#04H
	LCALL	CCC
	MOV	A,#10H
	LCALL	BBB
	LCALL	DE02S
	DJNZ	R2,TTT
	MOV	A,#61H
	LCALL	CCC
	MOV	A,#80H
	LCALL	BBB	
	LCALL	DE12S
	MOV	A,#20H
	LCALL	CCC
	MOV	A,#80H
	LCALL	BBB
	MOV	R2,#08H
GGG:	
	MOV	A,#0A2H
	LCALL	CCC
	LCALL	DE02S
	MOV	A,#20H
	LCALL	CCC
	LCALL	DE02S
	DJNZ	R2,GGG
	LJMP	LLL
	
	
DE12S:	
	MOV	R5,#120   
	LJMP	DE1
DE6S:	
	MOV	R5,#60
	LJMP	DE1
DE02S:	MOV	R5,#02H

DE1:	MOV	R6,#200
DE2:	MOV	R7,#126
DE3:	
	DJNZ	R7,DE3
	DJNZ	R6,DE2
	DJNZ	R5,DE1
	RET
	;返回指令
CCC:	
	MOV	DPTR,#C_8
	MOVX	@DPTR,A
	RET
BBB:	
	MOV	DPTR,#B_8
	MOVX	@DPTR,A
	RET
	END