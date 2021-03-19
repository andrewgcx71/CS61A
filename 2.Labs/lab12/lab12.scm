; Lab 14: Final Review

(define (compose-all funcs)
  'YOUR-CODE-HERE
  (define (helper x)
  (cond
  ( (null? funcs) x )
  ( else ((compose-all (cdr funcs)) ((car funcs) x)) )

)
)
  helper
)
