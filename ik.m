close all

mdl_baxter;

K_inv = 0.3*eye(6);

%initializing q
q = zeros(7,1);


% T_des = SE3(transl(.3,.5,.5)).T;
T_des = [1 0 0 0; 0 1 0 1 ; 0 0 1 1; 0 0 0 1];

T_curr = right.fkine(q).T;


counter = 0;
% every time through loop, we check position error and if we have run
% for 1000 iterations yet or not.
while (norm(T_des(1:3,4)- T_curr(1:3,4)) > 0.0001) && norm(T_des(1:3,3) - T_curr(1:3,3)) > .0001 && (counter < 1000)
    % update pose and jacobian for current q's
    T_curr = right.fkine(q).T;
    J = right.jacob0(q);
    
    %calculate error in pose and transform back to base frame.
%     delta = tr2delta(T_cur, T_des);
    TD = inv(T_curr) * T_des;
    delta = [TD(1:3,4); vex(TD(1:3,1:3) - eye(3))];
    
    R2base = T_curr(1:3,1:3);
%     delta_base = [R2base, zeros(3,3); zeros(3,3), R2base]*delta;
    top = [R2base, zeros(3,3)];
    bottom = [zeros(3,3), R2base];
    together = [top;bottom];
    delta_base = together * delta;
    
    %perform the pseudo-inverse method
%     q = q + J'*inv(J*J'+0.1^2*eye(6))*K_inv*delta_base;
    q = q + J' * inv(J * J' + (.1^2)*eye(6)) * K_inv * delta_base;
    
    right.plot(q')
    counter = counter + 1
end
