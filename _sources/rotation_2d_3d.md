---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Rotations and rotation matrices

## Rotations in two dimensions

See: [rotation in
2d](https://matthew-brett.github.io/teaching/rotation_2d.html) and [Wikipedia
on rotation matrices](https://en.wikipedia.org/wiki/Rotation_matrix).

In two dimensions, rotating a vector $\theta$ around the origin can be
expressed as a 2 by 2 transformation matrix:

$$
R(\theta) = \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta \\
\end{bmatrix}
$$

This matrix rotates column vectors by matrix multiplication on the left:

$$
\begin{bmatrix}
x' \\
y' \\
\end{bmatrix} = \begin{bmatrix}
\cos \theta & -\sin \theta \\
\sin \theta & \cos \theta \\
\end{bmatrix}\begin{bmatrix}
x \\
y \\
\end{bmatrix}
$$

The coordinates $(x',y')$ of the point $(x,y)$ after rotation are:

$$
x' = x \cos \theta - y \sin \theta \\
y' = x \sin \theta + y \cos \theta
$$

See [rotation in 2D] for a visual proof.

## Rotations in three dimensions

Rotations in three dimensions extend simply from two dimensions.

Consider a [right-handed] set of x, y, z axes, maybe forming the x axis with
your right thumb, the y axis with your index finger, and the z axis with your
middle finger. Now look down the z axis, from positive z toward negative z. You
see the x and y axes pointing right and up respectively, on a plane in front of
you. A rotation around z leaves z unchanged, but changes x and y according to
the 2D rotation formula above:

$$
R_z(\theta) =
\begin{bmatrix}
\cos \theta &  -\sin \theta & 0 \\
\sin \theta & \cos \theta & 0 \\
0 & 0 & 1 \\
\end{bmatrix}
$$

For a rotation around x, we look down from positive x to the y and z axes,
pointing right and up, respectively.  y replaces x in the 2D formula, and z
replaces y, to give:

$$
y' = y \cos \theta - z \sin \theta \\
z' = y \sin \theta + z \cos \theta
$$

$$
R_x(\theta) = \begin{bmatrix}
1 & 0 & 0 \\
0 & \cos \theta &  -\sin \theta \\[3pt]
0 & \sin \theta  &  \cos \theta \\[3pt]
\end{bmatrix}
$$

Now consider a rotation around the y axis.   We look from positive y down the
y axis to the z and x axes, pointing right and up respectively.  $z$ replaces
$x$ in the 2D formula, and $x$ replaces $y$:

$$
z' = z \cos \theta - x \sin \theta \\
x' = z \sin \theta + x \cos \theta
$$

$$
R_y(\theta) = \begin{bmatrix}
\cos \theta & 0 & \sin \theta \\[3pt]
0 & 1 & 0 \\[3pt]
-\sin \theta & 0 & \cos \theta \\
\end{bmatrix}
$$

We can combine rotations with matrix multiplication. For example, here is an
rotation of $gamma$ radians around the x axis:

$$
\begin{bmatrix}
x'\\
y'\\
z'\\
\end{bmatrix} =
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\gamma) & -\sin(\gamma) \\
0 & \sin(\gamma) & \cos(\gamma) \\
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
z\\
\end{bmatrix}
$$

We could then apply a rotation of $phi$ radians around the y axis:

$$
\begin{bmatrix}
x''\\
y''\\
z''\\
\end{bmatrix} =
\begin{bmatrix}
\cos(\phi) & 0 & \sin(\phi) \\
0 & 1 & 0 \\
-\sin(\phi) & 0 & \cos(\phi) \\
\end{bmatrix}
\begin{bmatrix}
x'\\
j'\\
k'\\
\end{bmatrix}
$$

We could also write the combined rotation as:

$$
\begin{bmatrix}
x''\\
y''\\
z''\\
\end{bmatrix} =
\begin{bmatrix}
\cos(\phi) & 0 & \sin(\phi) \\
0 & 1 & 0 \\
-\sin(\phi) & 0 & \cos(\phi) \\
\end{bmatrix}
\begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\gamma) & -\sin(\gamma) \\
0 & \sin(\gamma) & \cos(\gamma) \\
\end{bmatrix}
\begin{bmatrix}
x\\
y\\
z\\
\end{bmatrix}
$$

Because matrix multiplication is associative:

$$
\mathbf{Q} = \begin{bmatrix}
1 & 0 & 0 \\
0 & \cos(\gamma) & -\sin(\gamma) \\
0 & \sin(\gamma) & \cos(\gamma) \\
\end{bmatrix}
$$

$$
\mathbf{P} = \begin{bmatrix}
\cos(\phi) & 0 & \sin(\phi) \\
0 & 1 & 0 \\
-\sin(\phi) & 0 & \cos(\phi) \\
\end{bmatrix}
$$

$$
\mathbf{M} = \mathbf{P} \cdot \mathbf{Q}
$$

$$
\begin{bmatrix}
x''\\
y''\\
z''\\
\end{bmatrix} =
\mathbf{M}
\begin{bmatrix}
x\\
y\\
z\\
\end{bmatrix}
$$

$\mathbf{M}$ is the rotation matrix that encodes a rotation by
$\gamma$ radians around the x axis *followed by* a rotation by
$\phi$ radians around the y axis.  We know that the y axis rotation
follows the x axis rotation because matrix multiplication operates from right
to left.
