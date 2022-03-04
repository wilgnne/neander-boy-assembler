.data              ; start of data section
    X: .word 3
    Y: .word 2
    Z: .word 0
.text              ; start of text section
    main:          ; main function
        LDA X      ; o acumulador recebe o valor de X
        ADD Y      ; o acumulador é somado com Y
        STA Z      ; o acumulador é copiado para Z
        HLT        ; o processador para
