alias.clear()
trigger.clear()

-- combat aliases --


alias.add("^sc(.*)$", function(m)
    mud.send("scan " ..  m[2])
end)

-- piloting aliases --

alias.add("^st$", function(m)
    mud.send("status")
end)

alias.add("^f$", function(m)
    mud.send("fire")
end)

alias.add("^fi$", function(m)
    mud.send("fire ion")
end)

alias.add("^fr$", function(m)
    mud.send("fire rocket")
end)

alias.add("^fm$", function(m)
    mud.send("fire missile")
end)

alias.add("^ft$", function(m)
    mud.send("fire torp")
end)

alias.add("^ch$", function(m)
    mud.send("chaff")
end)

alias.add("^p$", function(m)
    mud.send("prox")
end)

-- Launching set --

alias.add("^laun (.$)", function(matches)
    planet = matches[2]
    mud.send("launch")
end)

alias.add("^arka$", function(m)
    mud.send("calc perave 0 500 0")
end)

alias.add("^dant$", function(m)
    mud.send("calc raio 5200 390 -26550")
end)

-- triggers --

trigger.add("^The ship leaves the platform far behind as it flies into space.$", {}, function (m)
        mud.send("arka")
end)

trigger.add("^[Status]: Hyperspace calculations have been completed.$", {}, function(m)
	mud.send("hyper")
end)

-- Landing sets -- 

alias.add("^land (.*)$", function(m)
    if m[2] == "abort" then
        mud.send("land abort")
    end
    if m[2] == "arka" then
        mud.send("land arka alpha")
    end
    if m[2] == "dant" then
        mud.send("land dant jedi")
    end
    if m[2] == "tato" then
        mud.send("land " .. m[2] .. " mos")
    end
    if m[2] == "tato1" then
        mud.send('land tato [Praetorian-Class Frigate "Omni"] A Makeshift Landing Pad')
    end
end)

-- Ship sets --

alias.add("^xen$", function(m)
    mud.send("open Delta")
    mud.send("enter Delta")
    mud.send("close")
    mud.send("autopilot off")
    mud.send("pilot")
end)

alias.add("^xex$", function(m)
    mud.send("autopilot on")
    mud.send("open")
    mud.send("leave")
    mud.send("close Delta")
    mud.send("refuel Delta full")
end)


