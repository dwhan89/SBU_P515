import numpy as np
import matplotlib.pyplot as plt

# define x range
x = np.arange(0, 2.5* np.pi, 0.1)

# plot parami
alpha = 0.5

# plot regular sin plot

y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x,y, alpha=alpha, color = 'r')
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
plt.tight_layout()

plt.savefig("ac_none.png")

# plot R only

fig = plt.figure()
ax = fig.add_subplot(111)

v_r = np.sin(x)
i_r = 2.*np.sin(x)
ax.plot(x,v_r, alpha = alpha, color = 'r')
ax.plot(x,i_r, alpha = alpha, color = 'b')
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

ax.text(cos_t + 0.1 , cos_t - 0.1, r'$V_o$', fontsize=12)
ax.text(2*cos_t + 0.1 , 2*cos_t - 0.1, r'$I_o$', fontsize=12)
ax.text(cos_t, -0.2, r'$V(t)$', fontsize=12)
ax.text(2*cos_t, -0.2, r'$I(t)$', fontsize=12)
ax.text(0.2, 0.1, r'$\omega t$', fontsize=12)


hl = np.sqrt(3)
plt.xlim(-hl,hl)
plt.ylim(-hl,hl)

plt.tight_layout()

plt.savefig('phas_ro.png')

# plot C only

fig = plt.figure()
ax = fig.add_subplot(111)

v_r = np.sin(x)
i_r = 2.*np.sin(x + np.pi/2)
ax.plot(x,v_r, alpha = alpha, color = 'r')
ax.plot(x,i_r, alpha = alpha, color = 'b')
plt.axhline(y=1., color='k', linestyle='--')
plt.axhline(y=2., color='k', linestyle='--')

ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_color('none')

xlabels = ['T/4','T/2', '3T/4','T']
ylabels = [r'$V_R$', r'$I_R$']
plt.xticks(np.arange(np.pi/2,3.* np.pi, np.pi/2), xlabels, fontsize = 15)
plt.yticks([1,2], ylabels, fontsize = 15)

plt.xlabel('t', fontsize = 15)
ax.xaxis.set_label_coords(1.05, 0.5)

plt.xlim(0,2.5*np.pi)
plt.ylim(-2.5, 2.5)
plt.tight_layout()

plt.savefig('ac_co.png')

# plot C only phase

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

cos_t = np.cos(np.pi/4)
ax.arrow(0, 0, cos_t, cos_t, fc="r", ec="r",
                head_width=0.05, head_length=0.1 , alpha=alpha)
ax.arrow(0, 0, -2*cos_t, 2*cos_t, fc="b", ec="b",
                head_width=0.05, head_length=0.1 , alpha=alpha)
plt.plot([cos_t,cos_t],[0, cos_t], ls='--', color='k', alpha=0.5)  
plt.plot([-2*cos_t,-2*cos_t],[0, 2*cos_t], ls='--', color='k', alpha = 0.5)

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

ax.text(cos_t + 0.1 , cos_t - 0.1, r'$V_o$', fontsize=12)
ax.text(-2*cos_t + 0.1 , 2*cos_t - 0.1, r'$I_o$', fontsize=12)
ax.text(cos_t, -0.2, r'$V(t)$', fontsize=12)
ax.text(-2*cos_t, -0.2, r'$I(t)$', fontsize=12)
ax.text(0.2, 0.1, r'$\omega t$', fontsize=12)


hl = np.sqrt(3)
plt.xlim(-hl,hl)
plt.ylim(-hl,hl)

plt.tight_layout()

plt.savefig('phas_co.png')

plt.show(block = True)
