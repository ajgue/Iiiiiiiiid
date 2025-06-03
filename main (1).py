loadstring(game:HttpGet(("https://raw.githubusercontent.com/R7KScript/usernaxo/refs/heads/main/GUI3")))()
MakeWindow({
  Hub = {
    Title = "اسم",
    Animation = "جار التحميل... "
  },
  Key = {
    KeySystem = false,
    Title = "Key System",
    Description = "",
    KeyLink = "",
    Keys = {"1234"},
    Notifi = {
      Notifications = true,
      CorrectKey = "Running the Script...",
      Incorrectkey = "The key is incorrect",
      CopyKeyLink = "Copied to Clipboard"
    }
  }
})
MinimizeButton({
  Image = "rbxassetid://96720179320058",
  Size = {40, 40},
  Color = Color3.fromRGB(255, 125, 0),
  Corner = true,
  Stroke = false,
  StrokeColor = Color3.fromRGB(255, 125, 0)
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
}) 
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
loadstring(game:HttpGet(("https://raw.githubusercontent.com/R7KScript/usernaxo/refs/heads/main/GUI3")))()
MakeWindow({
  Hub = {
    Title = "اسم",
    Animation = "جار التحميل... "
  },
  Key = {
    KeySystem = false,
    Title = "Key System",
    Description = "",
    KeyLink = "",
    Keys = {"1234"},
    Notifi = {
      Notifications = true,
      CorrectKey = "Running the Script...",
      Incorrectkey = "The key is incorrect",
      CopyKeyLink = "Copied to Clipboard"
    }
  }
})
MinimizeButton({
  Image = "rbxassetid://96720179320058",
  Size = {40, 40},
  Color = Color3.fromRGB(255, 125, 0),
  Corner = true,
  Stroke = false,
  StrokeColor = Color3.fromRGB(255, 125, 0)
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
loadstring(game:HttpGet(("https://raw.githubusercontent.com/R7KScript/usernaxo/refs/heads/main/GUI3")))()
MakeWindow({
  Hub = {
    Title = "اسم",
    Animation = "جار التحميل... "
  },
  Key = {
    KeySystem = false,
    Title = "Key System",
    Description = "",
    KeyLink = "",
    Keys = {"1234"},
    Notifi = {
      Notifications = true,
      CorrectKey = "Running the Script...",
      Incorrectkey = "The key is incorrect",
      CopyKeyLink = "Copied to Clipboard"
    }
  }
})
MinimizeButton({
  Image = "rbxassetid://96720179320058",
  Size = {40, 40},
  Color = Color3.fromRGB(255, 125, 0),
  Corner = true,
  Stroke = false,
  StrokeColor = Color3.fromRGB(255, 125, 0)
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
loadstring(game:HttpGet(("https://raw.githubusercontent.com/R7KScript/usernaxo/refs/heads/main/GUI3")))()
MakeWindow({
  Hub = {
    Title = "اسم",
    Animation = "جار التحميل... "
  },
  Key = {
    KeySystem = false,
    Title = "Key System",
    Description = "",
    KeyLink = "",
    Keys = {"1234"},
    Notifi = {
      Notifications = true,
      CorrectKey = "Running the Script...",
      Incorrectkey = "The key is incorrect",
      CopyKeyLink = "Copied to Clipboard"
    }
  }
})
MinimizeButton({
  Image = "rbxassetid://96720179320058",
  Size = {40, 40},
  Color = Color3.fromRGB(255, 125, 0),
  Corner = true,
  Stroke = false,
  StrokeColor = Color3.fromRGB(255, 125, 0)
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
loadstring(game:HttpGet(("https://raw.githubusercontent.com/R7KScript/usernaxo/refs/heads/main/GUI3")))()
MakeWindow({
  Hub = {
    Title = "اسم",
    Animation = "جار التحميل... "
  },
  Key = {
    KeySystem = false,
    Title = "Key System",
    Description = "",
    KeyLink = "",
    Keys = {"1234"},
    Notifi = {
      Notifications = true,
      CorrectKey = "Running the Script...",
      Incorrectkey = "The key is incorrect",
      CopyKeyLink = "Copied to Clipboard"
    }
  }
})
MinimizeButton({
  Image = "rbxassetid://96720179320058",
  Size = {40, 40},
  Color = Color3.fromRGB(255, 125, 0),
  Corner = true,
  Stroke = false,
  StrokeColor = Color3.fromRGB(255, 125, 0)
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
loadstring(game:HttpGet(("https://raw.githubusercontent.com/R7KScript/usernaxo/refs/heads/main/GUI3")))()
MakeWindow({
  Hub = {
    Title = "اسم",
    Animation = "جار التحميل... "
  },
  Key = {
    KeySystem = false,
    Title = "Key System",
    Description = "",
    KeyLink = "",
    Keys = {"1234"},
    Notifi = {
      Notifications = true,
      CorrectKey = "Running the Script...",
      Incorrectkey = "The key is incorrect",
      CopyKeyLink = "Copied to Clipboard"
    }
  }
})
MinimizeButton({
  Image = "rbxassetid://96720179320058",
  Size = {40, 40},
  Color = Color3.fromRGB(255, 125, 0),
  Corner = true,
  Stroke = false,
  StrokeColor = Color3.fromRGB(255, 125, 0)
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})

-- زر: سكن بنية 2
AddButton(Main, {
    Name = "سكن بنية 2",
    Callback = function()
        ApplySkin({
            wearIds = {
                14592692650,
                82117306117807,
                137774587072189,
                77745292670615,
                101521377229190,
                139844681686463,
                17744851762,
                17577949104,
                91764783976162,
                13153798277,
                15461112727,
                120996397463893,
                113749281926930,
                2735240888
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    14960720067
                }
            }
        })
    end
})
local Main = MakeTab({Name = "تجربة"})
-- دالة لتطبيق السكن
function ApplySkin(skinData)
    local ReplicatedStorage = game:GetService("ReplicatedStorage")
    local RE = ReplicatedStorage:WaitForChild("RE", 10)
    local AvatarEvent = RE:WaitForChild("1Avata1rOrigina1l", 10)
    
    if AvatarEvent then
        AvatarEvent:FireServer("OCA")
    end

    for _, wearId in ipairs(skinData.wearIds) do
        wait(0.2)
        ReplicatedStorage.Remotes.Wear:InvokeServer(wearId)
    end

    if skinData.bodyData then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeCharacterBody:InvokeServer(skinData.bodyData)
    end

    if skinData.bodyColor then
        wait(0.3)
        ReplicatedStorage.Remotes.ChangeBodyColor:FireServer(skinData.bodyColor)
    end
end

-- زر: سكن بنية 1
AddButton(Main, {
    Name = "سكن بنيه 1",
    Callback = function()
        ApplySkin({
            wearIds = {
                104558184738792,
                110138817602297,
                78625340992085,
                133739083878132,
                15936091685,
                14960720067,
                11137846401,
                91764783976162,
                13900309877,
                9068015167,
                8428878750
            },
            bodyData = {
                [1] = {
                    115745153758680,
                    76683091425509,
                    75159926897589,
                    0,
                    0,
                    1
                }
            },
            bodyColor = "Institutional white"
        })
    end
})
