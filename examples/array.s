.data              ; start of data section
    X: .word 0     ; X is a array of 5 words
       .word 0
       .word 0
       .word 0
       .word 0
    Y: .word 10     ; Y is a word
.text              ; start of text section
    main:          ; main function
        LDA X      ; o acumulador recebe o valor de X
        ADD Y      ; o acumulador é somado com Y
        STA X      ; o acumulador é copiado para Z
        HLT        ; o processador para
