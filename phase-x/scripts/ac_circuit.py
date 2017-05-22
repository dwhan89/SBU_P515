import numpy as np
import matplotlib.pyplot as plt

# define x range
x = np.arange(0, 2.5* np.pi, 0.1)

# plot parami
alpha = 0.5

# plot regular sin plot

y = np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x,y, alpha=alpha, color = 'r', label=r'V(t)')
plt.axhline(y=1., color='k', linestyle='--')
plt.axhline(y=-1., color='k', linestyle='--')

ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

xlabels = ['T/2','T']
ylabels = [r'$-V_o$', r'$V_o$'] 
plt.xticks(np.arange(np.pi,3.* np.pi, np.pi), xlabels, fontsize = 15)
plt.yticks([-1,1], ylabels, fontsize = 15)

plt.xlabel('t', fontsize = 15)
plt.ylabel('V(t)', fontsize = 15, rotation = 0)
ax.xaxis.set_label_coords(1.05, 0.5)
ax.yaxis.set_label_coords(0, 1.05)

plt.xlim(0,2.5*np.pi)
plt.ylim(-1.5, 1.5)

plt.legend(loc="lower left", prop={'size':15})
plt.tight_layout()

plt.savefig("ac_none.png")

# plot R only

fig = plt.figure()
ax = fig.add_subplot(111)

v_r = np.cos(x)
i_r = 2.*np.cos(x)
ax.plot(x,v_r, alpha = alpha, color = 'r', label=r'$V_R(t)$')
ax.plot(x,i_r, alpha = alpha, color = 'b', label=r'$I_R(t)$')
plt.axhline(y=1., color='k', linestyle='--')
plt.axhline(y=2., color='k', linestyle='--')

ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

xlabels = ['T/2','T']
ylabels = [r'$V_R$', r'$I_R$']
plt.xticks(np.arange(np.pi,3.* np.pi, np.pi), xlabels, fontsize = 15)
plt.yticks([1,2], ylabels, fontsize = 15)

plt.xlabel('t', fontsize = 15)
ax.xaxis.set_label_coords(1.05, 0.5)

plt.xlim(0,2.5*np.pi)
plt.ylim(-2.5, 2.5)

plt.legend(loc="lower left", prop={'size':15})
plt.tight_layout()

plt.savefig("ac_ro.png")

# plot R only phase

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

cos_t = np.cos(np.pi/4)
ax.arrow(0, 0, cos_t, cos_t, fc="r", ec="r",
        head_width=0.05, head_length=0.1 , alpha=1)
ax.arrow(0, 0, 2*cos_t, 2*cos_t, fc="b", ec="b",
        head_width=0.05, head_length=0.1 , alpha=alpha)
plt.plot([cos_t,cos_t],[0, cos_t], ls='--', color='k', alpha=0.5) 
plt.plot([2*cos_t,2*cos_t],[0, 2*cos_t], ls='--', color='k', alpha = 0.5)

ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

plt.xticks([])
plt.yticks([])

#plt.xlabel('in-phase', fontsize = 10)
#ax.xaxis.set_label_coords(1.05, 0.5)
#plt.ylabel('out-phase', fontsize = 10, rotation = 0)
#ax.yaxis.set_label_coords(0.5, 1.03)

ax.text(cos_t + 0.1 , cos_t - 0.1, r'$V_R$', fontsize=12)
ax.text(2*cos_t + 0.1 , 2*cos_t - 0.1, r'$I_R$', fontsize=12)
ax.text(cos_t, -0.2, r'$V(t)$', fontsize=12)
ax.text(2*cos_t, -0.2, r'$I(t)$', fontsize=12)
ax.text(0.2, 0.1, r'$\omega t$', fontsize=12)


hl = np.sqrt(3)
plt.xlim(-hl,hl)
plt.ylim(-hl,hl)

plt.legend(loc="lower left", prop={'size':10})
plt.tight_layout()

plt.savefig('phas_ro.png')

# plot C only

fig = plt.figure()
ax = fig.add_subplot(111)

v_c = np.cos(x)
v_r = 1.5*np.cos(x  + np.pi/2)
i_r = 2.*np.cos(x  + np.pi/2)
ax.plot(x,v_c, alpha = alpha, color = 'r', label=r'$V_C(t)$')
ax.plot(x,i_r, alpha = alpha, color = 'b', label=r'$I_C(t)$')
ax.plot(x,v_r, alpha = alpha, color = 'g', ls= '--', label=r'$I_R(t)$')
plt.axhline(y=1., color='k', linestyle='--')
plt.axhline(y=1.5, color='k', linestyle='--')
plt.axhline(y=2., color='k', linestyle='--')

ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

xlabels = ['T/4','T/2', '3T/4','T']
ylabels = [r'$V_C$', r'$V_R$', r'$I_C$']
plt.xticks(np.arange(np.pi/2,3.* np.pi, np.pi/2), xlabels, fontsize = 15)
plt.yticks([1, 1.5 , 2], ylabels, fontsize = 15)

plt.xlabel('t', fontsize = 15)
ax.xaxis.set_label_coords(1.05, 0.5)

plt.xlim(0,2.5*np.pi)
plt.ylim(-2.5, 2.5)

plt.legend(loc="lower left", prop={'size':15})
plt.tight_layout()

plt.savefig('ac_co.png')

# plot RC only phase

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

v_r = np.sqrt(2*(1.5*np.sqrt(2))**2) # sqrt2
v_c = np.sqrt(2*(np.sqrt(2))**2) # sqrt2
v_o = np.sqrt(v_r**2+ v_c**2)
phi = np.arccos(v_r/v_o)

v_rx = v_r*np.cos(phi)
v_ry = v_r*np.sin(phi)

v_cx = v_c*np.cos(phi -np.pi/2)
v_cy = v_c*np.sin(phi -np.pi/2)

v_ox = v_o
v_oy = 0
ax.arrow(0, 0, v_cx , v_cy, fc="r", ec="r",
                head_width=0.05, head_length=0.1 , alpha=alpha)
ax.arrow(0, 0, v_rx, v_ry, fc="g", ec="g",
                head_width=0.05, head_length=0.1 , alpha=alpha)
ax.arrow(0, 0, v_ox , v_oy, fc="b", ec="b",
               head_width=0.05, head_length=0.1 , alpha=1., lw=3)
plt.plot([v_rx,v_rx],[0, v_ry], ls='--', color='k', alpha=0.5)  
plt.plot([v_cx,v_cx],[0, v_cy], ls='--', color='k', alpha = 0.5)


ax.spines['left'].set_position('center')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

plt.xticks([])
plt.yticks([])

#plt.xlabel('in-phase', fontsize = 10)
#ax.xaxis.set_label_coords(1.05, 0.5)
#plt.ylabel('out-phase', fontsize = 10, rotation = 0)
#ax.yaxis.set_label_coords(0.5, 1.03)

ax.text(v_cx + 0.1 ,  v_cy - 0.1, r'$V_C$', fontsize=12)
ax.text(v_rx + 0.1 ,  v_ry - 0.1, r'$V_R$', fontsize=12)
#ax.text(v_ox + 0.1 , v_oy + 0.1, r'$V_o$', fontsize=12)
ax.text(v_cx, -0.3, r'$V_C(t)$', fontsize=12)
ax.text(v_rx, -0.3, r'$V_R(t)$', fontsize=12)
ax.text(v_ox + 0.1, -0.3, r'$V_o(t)$', fontsize=12)
#ax.text(0.2, 0.1, r'$\omega t$', fontsize=12)


hl = v_ox + 0.5
plt.xlim(-hl,hl)
plt.ylim(-hl,hl)

plt.tight_layout()

plt.savefig('phas_co.png')

plt.show(block = True)
