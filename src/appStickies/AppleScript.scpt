FasdUAS 1.101.10   ��   ��    k             l     ��  ��    @ : Set the application to monitor and the message to display     � 	 	 t   S e t   t h e   a p p l i c a t i o n   t o   m o n i t o r   a n d   t h e   m e s s a g e   t o   d i s p l a y   
  
 l     ����  r         m        �    S a f a r i  o      ���� 0 monitoredapp monitoredApp��  ��        l    ����  r        m       �   0 Y o u r   c u s t o m   m e s s a g e   h e r e  o      ����  0 displaymessage displayMessage��  ��        l    ����  r        m    	��
�� boovfals  o      ���� 0 showmessage showMessage��  ��        l     ��������  ��  ��         l     �� ! "��   ! @ : Function to check if the application is in the foreground    " � # # t   F u n c t i o n   t o   c h e c k   i f   t h e   a p p l i c a t i o n   i s   i n   t h e   f o r e g r o u n d    $ % $ i      & ' & I      �� (���� &0 isappinforeground isAppInForeground (  )�� ) o      ���� 0 appname appName��  ��   ' k     $ * *  + , + O      - . - r     / 0 / 6    1 2 1 n    
 3 4 3 1    
��
�� 
pnam 4 4   �� 5
�� 
pcap 5 m    ����  2 =    6 7 6 1    ��
�� 
pisf 7 m    ��
�� boovtrue 0 o      ���� 0 frontapp frontApp . m      8 8�                                                                                  sevs  alis    \  Macintosh HD               �_JBD ����System Events.app                                              �����_J        ����  
 cu             CoreServices  0/:System:Library:CoreServices:System Events.app/  $  S y s t e m   E v e n t s . a p p    M a c i n t o s h   H D  -System/Library/CoreServices/System Events.app   / ��   ,  9�� 9 Z    $ : ;�� < : =    = > = o    ���� 0 frontapp frontApp > o    ���� 0 appname appName ; L     ? ? m    ��
�� boovtrue��   < L   " $ @ @ m   " #��
�� boovfals��   %  A B A l     ��������  ��  ��   B  C D C l     �� E F��   E N H Main loop to continuously check if the application is in the foreground    F � G G �   M a i n   l o o p   t o   c o n t i n u o u s l y   c h e c k   i f   t h e   a p p l i c a t i o n   i s   i n   t h e   f o r e g r o u n d D  H I H l   A J���� J V    A K L K k    < M M  N O N Z    6 P Q���� P I    �� R���� &0 isappinforeground isAppInForeground R  S�� S o    ���� 0 monitoredapp monitoredApp��  ��   Q k    2 T T  U V U I   "������
�� .miscactvnull��� ��� null��  ��   V  W X W I  # .�� Y Z
�� .sysodlogaskr        TEXT Y o   # $����  0 displaymessage displayMessage Z �� [ \
�� 
btns [ J   % ( ] ]  ^�� ^ m   % & _ _ � ` `  O K��   \ �� a��
�� 
dflt a m   ) * b b � c c  O K��   X  d e d l  / /�� f g��   f V P Wait until the application is no longer in the foreground before checking again    g � h h �   W a i t   u n t i l   t h e   a p p l i c a t i o n   i s   n o   l o n g e r   i n   t h e   f o r e g r o u n d   b e f o r e   c h e c k i n g   a g a i n e  i�� i r   / 2 j k j m   / 0��
�� boovtrue k o      ���� 0 showmessage showMessage��  ��  ��   O  l m l l  7 7�� n o��   n   Check every second    o � p p &   C h e c k   e v e r y   s e c o n d m  q�� q I  7 <�� r��
�� .sysodelanull��� ��� nmbr r m   7 8���� ��  ��   L =    s t s o    ���� 0 showmessage showMessage t m    ��
�� boovfals��  ��   I  u�� u l     ��������  ��  ��  ��       �� v w x��   v ������ &0 isappinforeground isAppInForeground
�� .aevtoappnull  �   � **** w �� '���� y z���� &0 isappinforeground isAppInForeground�� �� {��  {  ���� 0 appname appName��   y ������ 0 appname appName�� 0 frontapp frontApp z  8���� |��
�� 
pcap
�� 
pnam |  
�� 
pisf�� %� *�k/�,�[�,\Ze81E�UO��  eY f x �� }���� ~ ��
�� .aevtoappnull  �   � **** } k     A � �  
 � �   � �   � �  H����  ��  ��   ~     �� ���������� _�� b�������� 0 monitoredapp monitoredApp��  0 displaymessage displayMessage�� 0 showmessage showMessage�� &0 isappinforeground isAppInForeground
�� .miscactvnull��� ��� null
�� 
btns
�� 
dflt�� 
�� .sysodlogaskr        TEXT
�� .sysodelanull��� ��� nmbr�� B�E�O�E�OfE�O 4h�f *�k+  *j O���kv��� OeE�Y hOkj [OY�� ascr  ��ޭ