C=============================================================================C
! This program converts a file of coordinates (.gro) GROMACS into file of     !
! coordinates for fort.5 OCCAM. To make the convesion you need to add         !
! additional information. See the example at bottom of the file.              !
!                                                                             !
! Written by: Antonio De Nicola                                               !
! Version 1.2                                                                 !
! 31.08.2010                                                                  !
!                                                                             !
! Contacts: adenicola.chem@gmail.com                                          !
C=============================================================================C

      Program gro2occam    
      implicit none
      
      integer Natoms, NmolA, NatomA
      integer i, j, k, typeAtom, dt
      integer, allocatable:: Resindex(:), Atomindex(:), 
     + pa(:), c1a(:), c2a(:), c3a(:), c4a(:), c5a(:), c6a(:), 
     + c1b(:), c2b(:), c3b(:), c4b(:), c5b(:), c6b(:), 
     + nlegA(:), typeA(:) 
      Character*5, allocatable::  labA(:), labRes(:), labAtom(:)     
      real bx, by, bz
      real, allocatable::  x(:), y(:), z(:)                 
      real t                                              

      write(6,*)'Insert Box:'
      read(5,*) bx, by, bz
      write(6,*)'Nmol:'
      read(5,*) NmolA                      
      write(6,*)'Natom:'
      read(5,*) NatomA                 
      write(6,*)'delta no.'
      read(5,*) dt

      Natoms = NatomA*NmolA
    
      allocate(Resindex(Natoms))
      allocate(Atomindex(Natoms))
      allocate(labA(Natoms))
      allocate(labRes(Natoms))
      allocate(labAtom(Natoms))
      allocate(x(Natoms))
      allocate(y(Natoms))
      allocate(z(Natoms))
      allocate(pa(NatomA))
      allocate(c1a(NatomA))
      allocate(c2a(NatomA))
      allocate(c3a(NatomA))
      allocate(c4a(NatomA))
      allocate(c5a(NatomA))
      allocate(c6a(NatomA))
      allocate(nlegA(NatomA))
      allocate(typeA(NatomA))
      allocate(c1b(NatomA))
      allocate(c2b(NatomA))
      allocate(c3b(NatomA))
      allocate(c4b(NatomA))
      allocate(c5b(NatomA))
      allocate(c6b(NatomA))
      

      open (unit = 2, file = 'con.occ', status = 'OLD',
     $     access='SEQUENTIAL', form = 'FORMATTED')

      open (unit = 9, file = 'fort.5', status = 'UNKNOWN',
     $      form = 'FORMATTED')

      open (unit = 7, file = 'confout.gro', status = 'OLD',
     $     access='SEQUENTIAL', form = 'FORMATTED')

    
      read(2,*)
      read(2,*)
      do i=1, NatomA
       read(2,*) pa(i), typeA(i), c1a(i), c2a(i), c3a(i), c4a(i),
     $ c5a(i), c6a(i), labA(i), nlegA(i)
      enddo

      read(7,*)
      read(7,*)
      do i=1, Natoms
        read(7,101) Resindex(i), labRes(i), labAtom(i), Atomindex(i), 
     $ x(i), y(i), z(i)
        write(*,*) Resindex(i), labRes(i), labAtom(i), Atomindex(i), 
     $ x(i), y(i), z(i)
      enddo

      t=0.00000

      write(9,*) 'box:'
      write(9,*) bx, by, bz, t                                 
      write(9,*) 'Numero totale di molecole:'
      write(9,*) NmolA


C     MOLECOLE A                                                 
      do i=1, NmolA
         write(9,*) 'molecola nr. ', i
         write(9,*) NatomA
         do j=1, NatomA
             if(c1a(j).ne.0) then
                c1b(j) = c1a(j)+(NatomA*(i-1)) + dt
             endif
             if(c2a(j).ne.0) then
                c2b(j) = c2a(j)+(NatomA*(i-1)) + dt
             endif
             if(c3a(j).ne.0) then
                c3b(j) = c3a(j)+(NatomA*(i-1)) + dt
             endif
             if(c4a(j).ne.0) then
                c4b(j) = c4a(j)+(NatomA*(i-1)) + dt
             endif
             if(c5a(j).ne.0) then
                c5b(j) = c5a(j)+(NatomA*(i-1)) + dt
             endif
             if(c6a(j).ne.0) then
                c6b(j) = c6a(j)+(NatomA*(i-1)) + dt
             endif

             write(9,102) j+(NatomA*(i-1))+dt, 
     $ labA(j), typeA(j), nlegA(j),
     $ x(j+((i-1)*NatomA)), y(j+((i-1)*NatomA)), z(j+((i-1)*NatomA)), 
     $ c1b(j), c2b(j), c3b(j), c4b(j), c5b(j), c6b(j)

           do k =1,NatomA
              c1b(k) = 0
              c2b(k) = 0
              c3b(k) = 0
              c4b(k) = 0
              c5b(k) = 0
              c6b(k) = 0
           enddo
         enddo
      enddo

101   format(i5, 2a5, i5, 3f8.4)
102   format(i7, 1x, 1a5, 1i5, 2x, 1i5, 3f9.3, 4x, 6i7)  ! cambiato i5 in i7 e 2x in 1x

      endprogram
