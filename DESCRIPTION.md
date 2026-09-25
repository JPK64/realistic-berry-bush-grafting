# Realistic Berry Bush Grafting

This is a mod that allows you to combine berry bush graftings in a
somewhat realistic fashion.

## Grafting Process

Combine two berry bush cuttings (one being the scion, the other being
the rootstock), a knife and seaweed in the crafting grid like this:

```
+---------+-----------+
| Seaweed | Scion     |
+---------+-----------+
| Knife   | Rootstock |
+---------+-----------+
```

This will graft the scion onto the rootstock, resulting in a grafted
cutting with the combined traits of both. The grafted cutting then has
to be sealed inside a barrel of weak tannin for 2 days, consuming one
liter of tannin and turning it back into a regular old berry bush
cutting with the combined traits of both input cuttings.

### Which cuttings can be grafted onto which other cuttings

You can always graft cuttings onto a cutting of the same type, i.e.
strawberry cuttings onto other strawberry cuttings. Additionally, some
berry bushes of different types belong to the same plant family and can
be grafted onto all other cuttings from the same family, not just
cuttings of the same type:

- **Currants:** Blackcurrant, redcurrant and whitecurrant.
- **Brambles:** Blackberry, cloudberry and raspberry.
- **Heathers:** Blueberry and cranberry.

### How traits are combined

- If either cutting has a trait, then the grafted cutting will also get
  that trait.
- If both cuttings have the same trait, then the grafted cutting will
  get that trait only once.
- If one cutting has a positive trait and the other the negative trait
  of the same category, both traits cancel out, and the grafted cutting
  will get neither trait.

## Caveats

Due to the way the game works, this mod has to add 26,960 grid recipes
and 81 barrel recipes to the game. On somewhat good hardware, this will
add about 30 seconds of loading when entering a world or starting a
server.

Additionally, while the game does group recipes with the same berry bush
traits in the handbook, I could not find a way to make the game further
group recipes with the same cutting type but different traits, meaning
that each combination of traits is listed separately in certain places,
cluttering parts of the handbook.

## Planned Features

- Binding material, disinfected with weak tannin.
- Rooting tonic instead of just using seaweed in the crafting grid.
  - Potentially a custom model for asealed barrel with a grafted
    cutting, if possible.
- A handbook entry explaining the grafting process in-game.
- A random chance that a graft fails, if possible.

## Additional Information

<p>
<details>
<summary>Why create this mod?</summary>

The odds of obtaining a perfect berry bush cutting with all four
positive traits in the base game are astronomically low.

When the game generates a berry bush, each of the four trait categories
has a 15% chance of being applied to the berry bush. When a trait
category is applied, the positive trait only has a 40% chance of being
picked, while the chance of the negative trait being picked instead are
60%. This results in a 15% \* 40% = 6% chance that the positive trait of
a category is applied to the bush, or a 6% ^ 4 = 0.001296% chance of all
four positive traits being picked.

To find a perfect berry bush, you have to check about 77,000 berry
bushes on average. To 99% guarantee a perfect berry bush cutting, you
have to check about 355,000 berry bushes. And that is only for one of
the berries, and even if you do find such a berry bush, propagating it
will still take several in-game years.

I am a fan of realistic and somewhat challenging game mechanics. I am
not a fan of basically being unable to guarantee the perfect outcome.
That is why I created this mod.
</details>
</p>

<p>
<details>
<summary>Why not use the already existing mod?</summary>

I am aware that
[Aimli\_](https://mods.vintagestory.at/show/user/61EC66E73ACA2136CEB3)
already implemented such a feature in their own
[grafting mod](https://mods.vintagestory.at/cuttingtraitgrafting). I
highly suggest checking that mod out if you want something more
lightweight than this mod.

Unfortunately, that mod was not the right solution for me, mainly due to
2 reasons:

1. It is not flexible enough. It only allows you to combine cuttings
   with one or two positive traits each. It does not allow you to
   combine negative traits, or cuttings with mixed traits.
2. I wanted something more realistic. Simply being able to put two
   cuttings into a crafting grid is a bit overpowered in my opinion.
</details>
</p>

<p>
<details>
<summary>What makes this mod realistic?</summary>

### Basics

When doing a graft in real-life, you try to combine two branches of some
kind of tree or bush such that the cambium - the green-ish thin layer
right beneath the bark - physically connects. To do so, you remove the
bark from one branch (the rootstock) and press another branch (the
scion) onto the rootstock such that the cambium lines up, then keep them
pressed together until the plant heals the wound by knitting the cambium
together.

### Bronze Age

To keep the branches pressed together, bronze-age farmers would bind
both branches together using soaked strips of inner bark, hemp or
leather strips, and then seal the wound with animal fat, beeswax or a
mixture of mud, clay, cow dung and resin to keep moisture in and air or
pests out.

Usually, this would be done by grafting one cutting onto another plant
that has already been planted, not just another cutting. Additionally,
the rootstock and scion plants have to be dormant so the scion does not
demand any water from the rootstock before the graft can heal.

You can also graft two cuttings, which is known as bench grafting. Bench
grafting is usually harder, though, because you need to control moisture
and the rootstock must sprout roots at the same time or before the scion
demands water. Otherwise, the plant will dry out and die. For it to
work, you would still usually plant the grafted, dormant cutting
directly after grafting.

The graft can also rot. While sealing it is one way to prevent that from
happening, disinfecting the binding or washing the grafted plant with an
antiseptic can help prevent this. Tannin is a way to do this, but only
the weak variant as strong tannin would kill the plant.

### Modern

In the modern day and age, we have hydroponic propagation. Instead of
planting the bench-grafted cutting into soil, you can suspend it in
water that is infused with nutrients and oxygen. As long as part of the
stem stays exposed to air (so the plant does not suffocate) and
sunlight, the plant will grow roots and pick up nutrients from the
water.

To create the nutrient-infused water, compost, seaweed or kelp are used.
Especially seaweed is packed with natural plant growth hormones like
cytokinins that stimulate root growth and cell divsion.

### Mod

This mod combines bronze-age technologies with modern hydroponic
propagation to make the bench-grafting process interesting and engaging.
While modern ways of creating a rooting tonic don't really fit into the
game, sealing compost, seaweed or kelp in a barrel to create it can be a
way to create a kind of crude rooting tonic.
</details>
</p>
